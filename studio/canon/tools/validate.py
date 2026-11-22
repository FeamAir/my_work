#!/usr/bin/env python3
"""Canon validator for the studio saga.

Standard library only. Reads every ```canon fenced block in studio/canon/**/*.md
(one block = one record, strict "key: value" lines, inline lists in [..]).
See studio/canon/README.md, section "Machine blocks".

Usage:
  python3 tools/validate.py                 # validate real canon (records without example: true)
  python3 tools/validate.py --examples      # validate only EXAMPLE records
  python3 tools/validate.py --mermaid HS-0001 [--spoilers]   # print family tree of a house
  python3 tools/validate.py --cast S02E03 CH-0001,CH-0007    # who of these can appear in the episode
  python3 tools/validate.py --knows CH-0001 S03E05           # which secrets the character knows by then
  python3 tools/validate.py --root PATH     # canon root (default: parent of tools/)

Exit code: 0 = no errors (warnings allowed), 1 = errors found, 2 = usage/parse failure.
"""
import argparse
import os
import re
import sys
from collections import defaultdict

# ---------------------------------------------------------------- parsing

FENCE_OPEN = re.compile(r"^```canon\s*$")
FENCE_CLOSE = re.compile(r"^```\s*$")
KEY_LINE = re.compile(r"^([a-z][a-z0-9_]*):(?:\s+(.*))?$")

ID_PATTERNS = {
    "character": r"CH-(EX-)?\d{4}",
    "house": r"HS-(EX-)?\d{3}",
    "place": r"PL-(EX-)?\d{4}",
    "event": r"EV-(EX-)?\d{4}",
    "secret": r"SEC-(EX-)?\d{3}",
    "term": r"TERM-(EX-)?\d{4}",
    "era": r"ERA-(EX-)?[A-Z]{1,6}",
    "calendar": r"CAL-(EX-)?[A-Z0-9]{1,8}",
    "episode": r"S\d{2}E\d{2}",
    "world_rule": r"RULE-(EX-)?\d{3}",
}
ID_RE = {k: re.compile("^" + v + "$") for k, v in ID_PATTERNS.items()}
ANY_REF = re.compile(r"^(CH|HS|PL|EV|SEC|TERM|ERA|RULE)-(EX-)?[A-Z0-9]+$")
EP_RE = re.compile(r"^S(\d{2})E(\d{2})$")
CANON_STATES = {"draft", "approved", "locked", "retconned"}
LIFE_STATES = {"alive", "dead", "missing", "presumed_dead", "captive", "revealed", "unborn"}
SECRET_STATES = {"sealed", "seeded", "revealed"}


class Record(dict):
    file = ""
    line = 0

    def where(self):
        return "%s:%d" % (self.file, self.line)


def parse_value(raw):
    raw = (raw or "").strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [unquote(x.strip()) for x in inner.split(",") if x.strip()]
    return unquote(raw)


def unquote(s):
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    if s in ("~", "null", ""):
        return ""
    return s


def load_records(root):
    records, problems = [], []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, root)
            with open(path, encoding="utf-8") as fh:
                lines = fh.read().splitlines()
            cur = None
            for i, line in enumerate(lines, 1):
                if cur is None:
                    if FENCE_OPEN.match(line):
                        cur = Record()
                        cur.file, cur.line = rel, i
                    continue
                if FENCE_CLOSE.match(line):
                    records.append(cur)
                    cur = None
                    continue
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                m = KEY_LINE.match(s)
                if not m:
                    problems.append("%s:%d: cannot parse line %r (expected 'key: value')" % (rel, i, s))
                    continue
                key, val = m.group(1), m.group(2)
                if key in cur:
                    problems.append("%s:%d: duplicate key %r in one block" % (rel, i, key))
                cur[key] = parse_value(val)
            if cur is not None:
                problems.append("%s:%d: unclosed ```canon block" % (rel, cur.line))
    return records, problems


# ---------------------------------------------------------------- calendar & dates

class Calendar:
    def __init__(self, cal, eras):
        self.month_days = [int(x) for x in cal.get("month_days", [])] or [30] * 12
        self.year_len = sum(self.month_days)
        self.eras = {}  # abbr -> abs year offset of year 1
        for e in eras:
            self.eras[e.get("abbr", "")] = int(e.get("abs_start", 0))

    DATE_RE = re.compile(r"^(~)?([A-Z]{1,6})\s+(\d+)(?:-(\d{1,2}))?(?:-(\d{1,2}))?$")

    def interval(self, text):
        """Return (earliest_day, latest_day) or raise ValueError. '~' widens by 1 year."""
        m = self.DATE_RE.match(text.strip())
        if not m:
            raise ValueError("bad date format %r (expected 'ERA YYYY[-MM[-DD]]', e.g. 'AE 412-03-15')" % text)
        approx, era, y, mo, d = m.groups()
        if era not in self.eras:
            raise ValueError("unknown era %r in date %r" % (era, text))
        y = int(y)
        if y < 1:
            raise ValueError("year must be >= 1 in %r" % text)
        base = (self.eras[era] + y - 1) * self.year_len
        if mo is None:
            lo, hi = base, base + self.year_len - 1
        else:
            mo = int(mo)
            if not 1 <= mo <= len(self.month_days):
                raise ValueError("month %d out of range in %r" % (mo, text))
            mstart = base + sum(self.month_days[: mo - 1])
            if d is None:
                lo, hi = mstart, mstart + self.month_days[mo - 1] - 1
            else:
                d = int(d)
                if not 1 <= d <= self.month_days[mo - 1]:
                    raise ValueError("day %d out of range in %r" % (d, text))
                lo = hi = mstart + d - 1
        if approx:
            lo, hi = lo - self.year_len, hi + self.year_len
        return lo, hi


def ep_key(ep):
    m = EP_RE.match(ep or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def split_at(item):
    """'CH-0001@S02E04' -> ('CH-0001', 'S02E04'); 'X' -> ('X', '')."""
    if "@" in item:
        a, b = item.split("@", 1)
        return a.strip(), b.strip()
    return item.strip(), ""


def split_colon(item):
    if ":" in item:
        a, b = item.split(":", 1)
        return a.strip(), b.strip()
    return item.strip(), ""


# ---------------------------------------------------------------- validator

class Validator:
    def __init__(self, records, examples):
        self.errors, self.warnings = [], []
        self.recs = [r for r in records if (str(r.get("example", "")).lower() == "true") == examples]
        self.by_id = {}
        self.by_type = defaultdict(list)
        self.cal = None

    def err(self, rec, msg):
        self.errors.append("ERROR   %s [%s] %s" % (rec.where() if rec is not None else "-", rec.get("id", "?") if rec is not None else "-", msg))

    def warn(self, rec, msg):
        self.warnings.append("WARNING %s [%s] %s" % (rec.where() if rec is not None else "-", rec.get("id", "?") if rec is not None else "-", msg))

    # ---- helpers
    def ref(self, rec, field, value, kinds):
        """Check that value is an existing id of one of the kinds."""
        if not value:
            return None
        target = self.by_id.get(value)
        if target is None:
            self.err(rec, "%s -> unknown id %r" % (field, value))
            return None
        if target.get("type") not in kinds:
            self.err(rec, "%s -> %r is a %s, expected %s" % (field, value, target.get("type"), "/".join(kinds)))
            return None
        if rec.get("canon") in ("approved", "locked") and target.get("canon") == "draft":
            self.warn(rec, "%s record references draft %s" % (rec.get("canon"), value))
        return target

    def date(self, rec, field):
        v = rec.get(field)
        if not v or v == "?":
            return None
        if self.cal is None:
            return None
        try:
            return self.cal.interval(v)
        except ValueError as e:
            self.err(rec, "%s: %s" % (field, e))
            return None

    def episode(self, rec, field, ep, allow_origin=False):
        if allow_origin and ep in ("origin", ""):
            return True
        if ep_key(ep) is None:
            self.err(rec, "%s: bad episode code %r (expected SxxEyy%s)" % (field, ep, " or 'origin'" if allow_origin else ""))
            return False
        if self.by_type["episode"] and ep not in self.by_id:
            self.warn(rec, "%s: episode %s is not yet in timeline.md" % (field, ep))
        return True

    def ep_interval(self, ep):
        e = self.by_id.get(ep)
        if not e or e.get("type") != "episode":
            return None
        a = self.date(e, "date_start")
        b = self.date(e, "date_end") or a
        if a and b:
            return a[0], b[1]
        return None

    # ---- main
    def run(self):
        self.index()
        self.setup_calendar()
        self.check_eras_episodes()
        self.check_places()
        self.check_houses()
        self.check_characters()
        self.check_genealogy()
        self.check_events()
        self.check_secrets()
        self.check_terms()
        self.check_rules()

    def index(self):
        for r in self.recs:
            t, i = r.get("type"), r.get("id")
            if not t or t not in ID_RE:
                self.err(r, "missing or unknown type %r (known: %s)" % (t, ", ".join(sorted(ID_RE))))
                continue
            if not i:
                self.err(r, "missing id")
                continue
            if not ID_RE[t].match(i):
                self.err(r, "id %r does not match pattern for %s (%s)" % (i, t, ID_PATTERNS[t]))
            if i in self.by_id:
                self.err(r, "duplicate id; first defined at %s" % self.by_id[i].where())
                continue
            c = r.get("canon")
            if c not in CANON_STATES:
                self.err(r, "canon must be one of %s, got %r" % (sorted(CANON_STATES), c))
            self.by_id[i] = r
            self.by_type[t].append(r)

    def setup_calendar(self):
        cals = self.by_type["calendar"]
        if len(cals) > 1:
            for c in cals[1:]:
                self.err(c, "more than one calendar record; only one is allowed")
        if not cals:
            if self.recs:
                self.warnings.append("WARNING - no calendar record; date checks skipped")
            return
        try:
            self.cal = Calendar(cals[0], self.by_type["era"])
        except ValueError as e:
            self.err(cals[0], "bad calendar: %s" % e)

    def check_eras_episodes(self):
        for e in self.by_type["era"]:
            if not re.match(r"^[A-Z]{1,6}$", e.get("abbr", "")):
                self.err(e, "era abbr must be 1-6 capital letters")
            if not re.match(r"^-?\d+$", str(e.get("abs_start", ""))):
                self.err(e, "era abs_start must be an integer")
        eps = sorted(self.by_type["episode"], key=lambda r: ep_key(r["id"]) or (0, 0))
        prev = None
        for e in eps:
            iv = self.ep_interval(e["id"])
            a = self.date(e, "date_start")
            b = self.date(e, "date_end")
            if a and b and b[1] < a[0]:
                self.err(e, "date_end is before date_start")
            if prev and iv and prev[1] and iv[1] < prev[1][0] and e.get("flashback") != "true":
                self.err(e, "episode is set before %s but not marked flashback: true" % prev[0])
            if iv and e.get("flashback") != "true":
                prev = (e["id"], iv)
            for f in ("pov",):
                for c in e.get(f, []) if isinstance(e.get(f), list) else []:
                    self.ref(e, f, c, ("character",))

    def check_places(self):
        for p in self.by_type["place"]:
            self.ref(p, "parent", p.get("parent"), ("place",))
            self.ref(p, "held_by", p.get("held_by"), ("house",))
        self.no_cycles("place", "parent", "place hierarchy")

    def check_houses(self):
        for h in self.by_type["house"]:
            self.ref(h, "seat", h.get("seat"), ("place",))
            for p in h.get("lands", []) or []:
                self.ref(h, "lands", p, ("place",))
            self.ref(h, "liege", h.get("liege"), ("house",))
            self.ref(h, "cadet_of", h.get("cadet_of"), ("house",))
            founder = self.ref(h, "founder", h.get("founder"), ("character",))
            fd, ex = self.date(h, "founded"), self.date(h, "extinct")
            if fd and ex and ex[1] < fd[0]:
                self.err(h, "extinct before founded")
            if founder and fd:
                b = self.date(founder, "born")
                if b and b[0] > fd[1]:
                    self.err(h, "founder %s born after the house was founded" % founder["id"])
            for item in h.get("heads", []) or []:
                cid, when = split_at(item)
                c = self.ref(h, "heads", cid, ("character",))
                if c and when and self.cal:
                    try:
                        w = self.cal.interval(when)
                    except ValueError as e:
                        self.err(h, "heads: %s" % e)
                        continue
                    b, d = self.date(c, "born"), self.date(c, "died")
                    if b and w[1] < b[0]:
                        self.err(h, "heads: %s becomes head (%s) before birth" % (cid, when))
                    if d and w[0] > d[1]:
                        self.err(h, "heads: %s becomes head (%s) after death" % (cid, when))
            for item in h.get("alliances", []) or []:
                hid, _ = split_colon(split_at(item)[0])
                self.ref(h, "alliances", hid, ("house",))
            for s in h.get("secrets", []) or []:
                self.ref(h, "secrets", s, ("secret",))
        self.no_cycles("house", "liege", "liege chain")
        self.no_cycles("house", "cadet_of", "cadet chain")

    def check_characters(self):
        names = defaultdict(list)
        pair_seen = {}
        for c in self.by_type["character"]:
            if not c.get("name"):
                self.err(c, "missing name")
            names[c.get("name", "").lower()].append(c)
            self.ref(c, "house", c.get("house"), ("house",))
            self.ref(c, "born_at", c.get("born_at"), ("place",))
            self.ref(c, "died_at", c.get("died_at"), ("place",))
            for f in ("father", "mother", "true_father", "true_mother"):
                self.ref(c, f, c.get(f), ("character",))
            for p in c.get("adoptive_parents", []) or []:
                self.ref(c, "adoptive_parents", p, ("character",))
            for f in ("true_father", "true_mother"):
                if c.get(f) and not c.get("parentage_secret"):
                    self.err(c, "%s set without parentage_secret (hidden parentage must be in secrets.md)" % f)
            self.ref(c, "parentage_secret", c.get("parentage_secret"), ("secret",))
            b, d = self.date(c, "born"), self.date(c, "died")
            if b and d and d[1] < b[0]:
                self.err(c, "died before born")
            for item in c.get("relations", []) or []:
                tid, kind = split_colon(item)
                if not kind:
                    self.err(c, "relations: %r has no kind (use ID:kind)" % item)
                if tid == c.get("id"):
                    self.err(c, "relations: relation to self")
                    continue
                if self.ref(c, "relations", tid, ("character",)):
                    key = tuple(sorted((c["id"], tid))) + (kind,)
                    if key in pair_seen:
                        self.warn(c, "relation %s:%s is also recorded at %s (one fact - one place)" % (tid, kind, pair_seen[key].where()))
                    else:
                        pair_seen[key] = c
            for s in c.get("secrets", []) or []:
                self.ref(c, "secrets", s, ("secret",))
            self.check_status_track(c, b, d)
        for n, lst in names.items():
            if n and len(lst) > 1:
                self.warn(lst[1], "same name as %s (%s) - make sure this is intended, add epithet" % (lst[0]["id"], lst[0].where()))

    def check_status_track(self, c, born, died):
        track = c.get("status_track", []) or []
        prev_key, prev_state = None, None
        dead_ep = None
        for item in track:
            ep, state = split_colon(item)
            if state not in LIFE_STATES:
                self.err(c, "status_track: unknown state %r (allowed: %s)" % (state, ", ".join(sorted(LIFE_STATES))))
            if not self.episode(c, "status_track", ep):
                continue
            k = ep_key(ep)
            if prev_key and k <= prev_key:
                self.err(c, "status_track: %s is not after the previous entry" % ep)
            if prev_state == "dead" and state != "dead" and c.get("may_return") != "true":
                self.err(c, "status_track: %s after dead at %s (set may_return: true only if world rules allow)" % (state, dead_ep))
            if state == "dead" and dead_ep is None:
                dead_ep = ep
            iv = self.ep_interval(ep)
            if iv and died and state == "alive" and died[1] < iv[0]:
                self.err(c, "status_track: alive at %s but died (%s) before that episode" % (ep, c.get("died")))
            if iv and born and state not in ("unborn",) and born[0] > iv[1]:
                self.err(c, "status_track: %s at %s but born (%s) after that episode" % (state, ep, c.get("born")))
            prev_key, prev_state = k, state
        if dead_ep:
            iv = self.ep_interval(dead_ep)
            if not died:
                self.warn(c, "dead at %s but no died date" % dead_ep)
            elif iv and died[0] > iv[1]:
                self.err(c, "dead at %s but died date %s is after that episode" % (dead_ep, c.get("died")))

    def check_genealogy(self):
        chars = {c["id"]: c for c in self.by_type["character"]}
        for c in chars.values():
            b = self.date(c, "born")
            for f in ("father", "mother", "true_father", "true_mother"):
                p = chars.get(c.get(f))
                if not p:
                    continue
                if p["id"] == c["id"]:
                    self.err(c, "%s is self" % f)
                    continue
                pb, pd = self.date(p, "born"), self.date(p, "died")
                if b and pb:
                    if pb[0] >= b[1]:
                        self.err(c, "%s %s born after child" % (f, p["id"]))
                    elif self.cal and (b[0] - pb[1]) < 12 * self.cal.year_len:
                        self.warn(c, "%s %s would be under 12 at child's birth" % (f, p["id"]))
                if b and pd:
                    grace = (self.cal.year_len if (self.cal and f in ("father", "true_father")) else 0)
                    if pd[1] + grace < b[0]:
                        self.err(c, "%s %s died before child was born" % (f, p["id"]))
            if c.get("father") and c.get("father") == c.get("true_father"):
                self.warn(c, "true_father equals father - remove true_father")
            if c.get("mother") and c.get("mother") == c.get("true_mother"):
                self.warn(c, "true_mother equals mother - remove true_mother")
        # cycles over all parent links (official + true + adoptive)
        graph = {cid: [x for x in (c.get("father"), c.get("mother"), c.get("true_father"), c.get("true_mother")) if x in chars]
                 + [x for x in (c.get("adoptive_parents") or []) if x in chars]
                 for cid, c in chars.items()}
        self.find_cycles(graph, "genealogy (ancestor of self)")

    def check_events(self):
        for e in self.by_type["event"]:
            d = self.date(e, "date")
            de = self.date(e, "date_end")
            if not e.get("date"):
                self.err(e, "event without date (use '?' if unknown)")
            if d and de and de[1] < d[0]:
                self.err(e, "date_end before date")
            span = (d[0], (de or d)[1]) if d else None
            if e.get("episode"):
                self.episode(e, "episode", e["episode"])
                iv = self.ep_interval(e["episode"])
                if iv and span and (span[1] < iv[0] or span[0] > iv[1]) and e.get("flashback") != "true":
                    self.err(e, "event date is outside the dates of %s (mark flashback: true if shown as flashback)" % e["episode"])
            self.ref(e, "place", e.get("place"), ("place",))
            for h in e.get("houses", []) or []:
                self.ref(e, "houses", h, ("house",))
            killed = set(e.get("killed", []) or [])
            for cid in (e.get("participants", []) or []) + sorted(killed):
                c = self.ref(e, "participants/killed", cid, ("character",))
                if not c or not span:
                    continue
                b, dd = self.date(c, "born"), self.date(c, "died")
                if b and b[0] > span[1]:
                    self.err(e, "%s takes part before being born (%s)" % (cid, c.get("born")))
                if dd and dd[1] < span[0]:
                    self.err(e, "%s takes part after death (%s)" % (cid, c.get("died")))
                if cid in killed:
                    if not dd:
                        self.err(e, "%s killed here but has no died date" % cid)
                    elif dd[1] < span[0] or dd[0] > span[1]:
                        self.err(e, "%s killed here but died date %s does not match event date" % (cid, c.get("died")))
            for s in e.get("secrets", []) or []:
                self.ref(e, "secrets", s, ("secret",))

    def check_secrets(self):
        for s in self.by_type["secret"]:
            if s.get("status") not in SECRET_STATES:
                self.err(s, "status must be one of %s" % sorted(SECRET_STATES))
            if not s.get("truth"):
                self.err(s, "missing truth")
            reveal = s.get("reveal")
            rk = None
            if reveal:
                if self.episode(s, "reveal", reveal):
                    rk = ep_key(reveal)
            else:
                self.warn(s, "no planned reveal episode (fine for long-term mysteries, but plan it)")
            hints = s.get("hints", []) or []
            last = None
            for h in hints:
                if not self.episode(s, "hints", h):
                    continue
                k = ep_key(h)
                if rk and k >= rk:
                    self.err(s, "hint %s is not before reveal %s" % (h, reveal))
                if last and k < last:
                    self.warn(s, "hints are not in episode order")
                last = k
            if s.get("status") == "seeded" and not hints:
                self.err(s, "status seeded but no hints listed")
            if rk and s.get("min_seasons_hidden"):
                first = ep_key(hints[0]) if hints and ep_key(hints[0]) else None
                if first and rk[0] - first[0] < int(s["min_seasons_hidden"]):
                    self.warn(s, "revealed after %d season(s) from first hint, planned at least %s" % (rk[0] - first[0], s["min_seasons_hidden"]))
            for item in s.get("known_by", []) or []:
                cid, when = split_at(item)
                c = self.ref(s, "known_by", cid, ("character",))
                if not when:
                    self.err(s, "known_by: %r needs @origin or @SxxEyy" % item)
                    continue
                if not self.episode(s, "known_by", when, allow_origin=True) or when == "origin" or not c:
                    continue
                iv = self.ep_interval(when)
                dd = self.date(c, "died")
                if iv and dd and dd[1] < iv[0]:
                    self.err(s, "known_by: %s learns at %s but is already dead" % (cid, when))
                for item2 in c.get("status_track", []) or []:
                    ep, st = split_colon(item2)
                    if st == "dead" and ep_key(ep) and ep_key(ep) < ep_key(when):
                        self.err(s, "known_by: %s learns at %s but is dead since %s" % (cid, when, ep))
            for r in s.get("related", []) or []:
                if not ANY_REF.match(r):
                    self.err(s, "related: %r is not an id" % r)
                else:
                    self.ref(s, "related", r, tuple(ID_RE))
            for d in s.get("depends_on", []) or []:
                dep = self.ref(s, "depends_on", d, ("secret",))
                if dep and rk and dep.get("reveal") and ep_key(dep["reveal"]) and ep_key(dep["reveal"]) > rk:
                    self.warn(s, "depends_on %s which is revealed later (%s)" % (d, dep["reveal"]))
        self.no_cycles("secret", "depends_on", "secret dependencies", multi=True)

    def check_terms(self):
        seen = {}
        covered = set()
        for t in self.by_type["term"]:
            term = t.get("term", "")
            if not term:
                self.err(t, "missing term")
            if not t.get("say"):
                self.err(t, "missing 'say' (respelling for voice synthesis)")
            k = term.lower()
            if k in seen:
                self.err(t, "term %r already defined at %s" % (term, seen[k].where()))
            seen[k] = t
            if t.get("ref"):
                if self.ref(t, "ref", t["ref"], tuple(ID_RE)):
                    covered.add(t["ref"])
        for typ in ("character", "house", "place"):
            for r in self.by_type[typ]:
                if r["id"] not in covered:
                    self.warn(r, "no glossary entry (pronunciation) for %s %r" % (typ, r.get("name", "")))

    def check_rules(self):
        for r in self.by_type["world_rule"]:
            if not r.get("rule"):
                self.err(r, "missing rule text")

    # ---- graph helpers
    def no_cycles(self, typ, field, label, multi=False):
        graph = {}
        for r in self.by_type[typ]:
            v = r.get(field)
            vals = v if isinstance(v, list) else ([v] if v else [])
            graph[r["id"]] = [x for x in vals if x in self.by_id]
        self.find_cycles(graph, label)

    def find_cycles(self, graph, label):
        WHITE, GREY, BLACK = 0, 1, 2
        color = {n: WHITE for n in graph}
        reported = set()

        def dfs(start):
            stack = [(start, iter(graph.get(start, [])))]
            path = [start]
            color[start] = GREY
            while stack:
                node, it = stack[-1]
                nxt = next(it, None)
                if nxt is None:
                    color[node] = BLACK
                    stack.pop()
                    path.pop()
                    continue
                if nxt not in color:
                    continue
                if color[nxt] == GREY:
                    cyc = path[path.index(nxt):] + [nxt]
                    key = frozenset(cyc)
                    if key not in reported:
                        reported.add(key)
                        self.err(self.by_id.get(nxt), "cycle in %s: %s" % (label, " -> ".join(cyc)))
                elif color[nxt] == WHITE:
                    color[nxt] = GREY
                    stack.append((nxt, iter(graph.get(nxt, []))))
                    path.append(nxt)

        for n in sorted(graph):
            if color[n] == WHITE:
                dfs(n)

    # ---- queries
    def mermaid(self, house_id, spoilers):
        chars = {c["id"]: c for c in self.by_type["character"]}
        members = {cid for cid, c in chars.items() if c.get("house") == house_id}
        # include parents of members so marriages into the house are visible
        for cid in list(members):
            for f in ("father", "mother") + (("true_father", "true_mother") if spoilers else ()):
                if chars[cid].get(f) in chars:
                    members.add(chars[cid][f])
        out = ["flowchart TD"]
        for cid in sorted(members):
            c = chars[cid]
            life = "%s - %s" % (c.get("born") or "?", c.get("died") or "")
            out.append('  %s["%s<br/>%s<br/>%s"]' % (cid.replace("-", "_"), c.get("name", cid), cid, life.strip(" -")))
        for cid in sorted(members):
            c = chars[cid]
            for f in ("father", "mother"):
                if c.get(f) in members:
                    out.append("  %s --> %s" % (c[f].replace("-", "_"), cid.replace("-", "_")))
            if spoilers:
                for f in ("true_father", "true_mother"):
                    if c.get(f) in members:
                        out.append("  %s -.->|true, %s| %s" % (c[f].replace("-", "_"), c.get("parentage_secret", "?"), cid.replace("-", "_")))
        return "\n".join(out)

    def state_at(self, c, ep):
        state = "unknown"
        for item in c.get("status_track", []) or []:
            e, s = split_colon(item)
            if ep_key(e) and ep_key(e) <= ep_key(ep):
                state = s
        iv = self.ep_interval(ep)
        b, d = self.date(c, "born"), self.date(c, "died")
        if iv and d and d[1] < iv[0]:
            state = "dead (by died date %s)" % c.get("died")
        if iv and b and b[0] > iv[1]:
            state = "unborn (born %s)" % c.get("born")
        return state

    def knows(self, cid, ep):
        res = []
        for s in self.by_type["secret"]:
            for item in s.get("known_by", []) or []:
                who, when = split_at(item)
                if who == cid and (when == "origin" or (ep_key(when) and ep_key(when) <= ep_key(ep))):
                    res.append("%s (since %s): %s" % (s["id"], when, s.get("truth", "")))
            if s.get("reveal") and ep_key(s["reveal"]) and ep_key(s["reveal"]) <= ep_key(ep) and s.get("public_on_reveal") == "true":
                res.append("%s (public since %s): %s" % (s["id"], s["reveal"], s.get("truth", "")))
        return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--examples", action="store_true", help="validate only records marked example: true")
    ap.add_argument("--mermaid", metavar="HOUSE_ID")
    ap.add_argument("--spoilers", action="store_true", help="with --mermaid: show true (secret) parentage")
    ap.add_argument("--cast", nargs=2, metavar=("EPISODE", "IDS"))
    ap.add_argument("--knows", nargs=2, metavar=("CHAR_ID", "EPISODE"))
    a = ap.parse_args()

    records, problems = load_records(a.root)
    v = Validator(records, a.examples)
    v.run()
    v.errors[:0] = ["ERROR   " + p for p in problems]

    if a.mermaid:
        print(v.mermaid(a.mermaid, a.spoilers))
        return 0
    if a.cast:
        ep, ids = a.cast
        bad = 0
        for cid in [x.strip() for x in ids.split(",") if x.strip()]:
            c = v.by_id.get(cid)
            if not c or c.get("type") != "character":
                print("%s: UNKNOWN ID" % cid)
                bad = 1
                continue
            st = v.state_at(c, ep)
            ok = st in ("alive", "revealed", "captive", "unknown")
            bad |= not ok
            print("%s %-24s %s%s" % (cid, c.get("name", ""), st, "" if ok else "   <-- CHECK"))
        return 1 if bad else 0
    if a.knows:
        for line in v.knows(*a.knows) or ["(nothing recorded)"]:
            print(line)
        return 0

    for line in v.errors + v.warnings:
        print(line)
    ns = "EXAMPLE" if a.examples else "canon"
    print("\n%s: %d records, %d errors, %d warnings" % (ns, len(v.recs), len(v.errors), len(v.warnings)))
    return 1 if v.errors else 0


if __name__ == "__main__":
    sys.exit(main())
