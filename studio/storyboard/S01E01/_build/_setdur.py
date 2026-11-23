import re,sys
def setdur(fn, changes):
    s=open(fn).read()
    ms=list(re.finditer(r'\n    S\(([0-9.]+),', s))
    out=s; off=0
    for idx,new in sorted(changes.items()):
        m=ms[idx-1]  # 1-based shot index
        a,b=m.start(1)+off, m.end(1)+off
        out=out[:a]+str(new)+out[b:]; off+=len(str(new))-(b-a)
    open(fn,'w').write(out)
