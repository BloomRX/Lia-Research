import subprocess,os,concurrent.futures as cf,sys
rows=[l.strip().split("|") for l in open("resolve.tsv")]
def cat(p):
    if '.agents/' in p: return 'SKILL'
    if '/adr/' in p or 'ADR-' in p or 'DECISION' in p.upper() or 'decisions/' in p: return 'DECISION'
    if 'docs/research' in p or 'RESEARCH' in p: return 'RESEARCH'
    if 'docs/reports' in p or 'REPORT' in p or 'AUDIT' in p: return 'REPORT'
    if 'docs/architecture' in p or 'ARCHITECTURE' in p: return 'ARCH'
    if 'licen' in p.lower() or 'provenance' in p.lower() or 'NOTICE' in p: return 'LICENSE'
    if 'docs/plans' in p or 'planejamento' in p or 'PLAN' in p: return 'PLAN'
    return 'OTHER'
sel=[r for r in rows if cat(r[2]) in ('RESEARCH','REPORT','ARCH','DECISION','LICENSE') and int(r[3])<=160000]
sel+= [r for r in rows if r[2].endswith('docs/README.md') or r[2].endswith('README.md') and int(r[3])<12000]
print("targets:",len(sel),file=sys.stderr)
def raw(repo,path,ref):
    p=subprocess.run(["gh","api","-H","Accept: application/vnd.github.raw",f"repos/BloomRX/{repo}/contents/{path}?ref={ref}"],capture_output=True,text=True)
    return p.stdout if p.returncode==0 else None
def work(r):
    repo,br,path,size,date=r
    txt=raw(repo,path,br)
    if txt is None: return False,repo,path
    d=f"corpus/{repo}"; os.makedirs(d,exist_ok=True)
    open(os.path.join(d,path.replace("/","__")),"w").write(txt)
    return True,repo,path
ok=0;bad=[]
with cf.ThreadPoolExecutor(6) as ex:
    for good,repo,path in ex.map(work,sel):
        if good: ok+=1
        else: bad.append((repo,path))
print("ok",ok,"of",len(sel))
for b in bad[:15]: print("FAILED",b)
