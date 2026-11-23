"""Shot data helper for the S01E01 storyboard generator.

Each scene module defines SCENE (dict) and SHOTS (list of S(...)).
build.py numbers the shots (step 10), computes timecodes, models, costs
and checks studio rules. No network, no paid calls.
"""


class S:
    def __init__(self, dur, plan, cam, act, line, cls, la, refs, kf, mot, dirn,
                 key=None, reuse=None, clipreuse=None, clip=None, l12=0,
                 nochar=False, refplate=False, vfx=None, v=None, tags=(),
                 note=None):
        self.dur = float(dur)
        self.plan = plan
        self.cam = cam
        self.act = act
        self.line = line
        self.cls = cls
        self.la = la
        self.refs = refs
        self.kf = kf
        self.mot = mot
        self.dirn = dirn
        self.key = key
        self.reuse = reuse          # key of a shot whose keyframe/plate is reused (no new image)
        self.clipreuse = clipreuse  # key of a shot whose generated clip is reused (no new video)
        self.clip = clip            # generated clip length, s (default per class)
        self.l12 = l12              # extra L-12 drawings (edits)
        self.nochar = nochar        # no characters in frame -> NB, animatic image may be final
        self.refplate = refplate    # plate comes ready from the reference set (tapestry, map, title)
        self.vfx = vfx              # ID from studio/vfx/pilot_vfx_shots.md
        self.v = v                  # vertical cut tag V1..V5
        self.tags = set(tags)       # 'stone', 'cord', 'ring', 'lip'
        self.note = note
        self.id = None
        self.tc = None
        self.scene = None
