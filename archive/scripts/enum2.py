import json, subprocess, sys, concurrent.futures as cf
REPOS = {"Lia-Project":"proj","Lia-Forge":"forge","Lia-Studio":"studio","Lia-AgentHub":"hub","Lia-Model-Lab":"lab"}
def gh(args):
    return subprocess.run(["gh"]+args, capture_output=True, text=True).stdout
def branches(n):
    out = gh(["api", f"repos/BloomRX/{n}/branches", "--paginate", "--jq", '[.[] | {name:.name, sha:.commit.sha}]'])
    return json.loads(out or "[]")
def tree(n, sha):
    out = gh(["api", f"repos/BloomRX/{n}/git/trees/{sha}?recursive=1"])
    try: return json.loads(out).get("tree", [])
    except Exception: return []
tasks = []
for n in REPOS:
    for b in branches(n):
        tasks.append((n, b["name"], b["sha"]))
print(f"branches: {len(tasks)}", file=sys.stderr)
def work(t):
    n, bn, sha = t
    return [(n, bn, sha[:10], e["size"] if "size" in e else 0, e["path"]) for e in tree(n, sha) if e["type"]=="blob"]
rows = []
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(work, tasks):
        rows.extend(r)
with open("/tmp/inv/all_files.tsv","w") as f:
    for r in rows: f.write("\t".join(map(str,r))+"\n")
print(f"files: {len(rows)}", file=sys.stderr)
