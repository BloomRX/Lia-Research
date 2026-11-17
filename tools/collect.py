import json, subprocess, os, concurrent.futures as cf

TARGETS = [
    ("open-jarvis/OpenJarvis", "openjarvis"),
    ("vercel-labs/ui", "vercel-ui"),
    ("anefzaoui/misterdownloadmanager", "misterdl"),
    ("tradermonty/claude-trading-skills", "trading-skills"),
    ("homeassistant-ai/ha-mcp", "ha-mcp"),
    ("l0ng-ai/openidea", "openidea"),
    ("islandmed/SculptForge", "sculptforge"),
    ("Donchitos/Claude-Code-Game-Studios", "cc-game-studios"),
    ("academa-labs/manimgx", "manimgx"),
    ("Ryder-Sun/Meldwork", "meldwork"),
    ("backnotprop/plannotator", "plannotator"),
    ("patch-gg/pixelfx", "pixelfx"),
    ("theclaymethod/unslop", "unslop"),
    ("elayadesign/ai-design-skills", "ai-design-skills"),
]


def gh(args, jq=None):
    a = ["gh", "api"] + args + (["--jq", jq] if jq else [])
    p = subprocess.run(a, capture_output=True, text=True)
    return p.stdout


def raw(repo, path, ref=None):
    u = "repos/%s/contents/%s" % (repo, path) + (("?ref=" + ref) if ref else "")
    p = subprocess.run(["gh", "api", "-H", "Accept: application/vnd.github.raw", u],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None


META_JQ = '{name:.full_name,desc:.description,lic:.license.spdx_id,licname:.license.name,stars:.stargazers_count,forks:.forks_count,pushed:.pushed_at,created:.created_at,archived:.archived,lang:.language,topics:.topics,home:.homepage,default:.default_branch,issues:.open_issues_count,size:.size}'


def work(t):
    repo, slug = t
    d = "/tmp/ext/" + slug
    os.makedirs(d, exist_ok=True)
    meta = gh(["repos/" + repo], META_JQ)
    open(d + "/meta.json", "w").write(meta)
    try:
        m = json.loads(meta)
    except Exception:
        return (slug, "METAFAIL")
    br = m.get("default") or "main"
    sha_out = gh(["repos/%s/commits/%s" % (repo, br)], '{sha:.sha,date:.commit.committer.date,msg:.commit.message}')
    open(d + "/head.json", "w").write(sha_out)
    try:
        sha = json.loads(sha_out)["sha"]
    except Exception:
        sha = None
    if sha:
        tree = gh(["repos/%s/git/trees/%s?recursive=1" % (repo, sha)])
        open(d + "/tree.json", "w").write(tree)
        rel = gh(["repos/%s/releases?per_page=3" % repo], '[.[]|{tag:.tag_name,date:.published_at,name:.name}]')
        open(d + "/releases.json", "w").write(rel)
        for f in ["README.md", "readme.md", "README.rst"]:
            c = raw(repo, f, sha)
            if c:
                open(d + "/README.md", "w").write(c)
                break
        for lf in ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "NOTICE"]:
            c = raw(repo, lf, sha)
            if c:
                open(d + "/LICENSE_FILE", "w").write(c)
                break
        for mf in ["package.json", "pyproject.toml", "Cargo.toml", "go.mod", "requirements.txt"]:
            c = raw(repo, mf, sha)
            if c:
                open(d + "/MF_" + mf.replace(".", "_"), "w").write(c[:60000])
    return (slug, "ok sha=" + (sha or "?")[:10])


with cf.ThreadPoolExecutor(4) as ex:
    for slug, st in ex.map(work, TARGETS):
        print("%-18s %s" % (slug, st))
