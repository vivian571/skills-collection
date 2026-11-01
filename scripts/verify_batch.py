#!/usr/bin/env python3
"""Batch GitHub verification for daily skills harvest. Prints one compact JSON line per call."""
import json, subprocess, sys

GH = "/home/hatch/workspace/custom-connectors/custom.github/bin/gh_api.py"

def api(path):
    r = subprocess.run(["python3", GH, "GET", path], capture_output=True, text=True, timeout=90)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"status": -1, "body": {"error": r.stdout[:300] + r.stderr[:300]}}

def repo_meta(full):
    d = api(f"/repos/{full}")
    b = d.get("body", {})
    if d.get("status") != 200:
        return {"repo": full, "ok": False, "status": d.get("status"), "msg": str(b.get("message", b))[:120]}
    lic = b.get("license") or {}
    return {"repo": full, "ok": True, "stars": b.get("stargazers_count"),
            "license": lic.get("spdx_id"), "pushed": (b.get("pushed_at") or "")[:10],
            "branch": b.get("default_branch"), "desc": (b.get("description") or "")[:200]}

def tree_count(full, branch):
    d = api(f"/repos/{full}/git/trees/{branch}?recursive=1")
    b = d.get("body", {})
    if d.get("status") != 200:
        return {"repo": full, "tree_ok": False, "status": d.get("status"),
                "msg": str(b.get("message", b))[:120], "truncated": b.get("truncated")}
    paths = [t["path"] for t in b.get("tree", []) if t.get("type") == "blob"]
    skills = [p for p in paths if p.endswith("/SKILL.md") or p == "SKILL.md"]
    return {"repo": full, "tree_ok": True, "truncated": b.get("truncated"),
            "skill_md_count": len(skills), "skill_paths": skills[:40]}

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "search":
        q = sys.argv[2]
        d = api(f"/search/repositories?q={q}&sort=pushed&order=desc&per_page=20")
        b = d.get("body", {})
        items = b.get("items", [])
        print(json.dumps({"status": d.get("status"), "total": b.get("total_count"),
                          "items": [{"repo": i["full_name"], "stars": i["stargazers_count"],
                                     "license": (i.get("license") or {}).get("spdx_id"),
                                     "pushed": (i.get("pushed_at") or "")[:10],
                                     "branch": i.get("default_branch"),
                                     "desc": (i.get("description") or "")[:160]} for i in items]},
                         ensure_ascii=False))
    elif mode == "verify":
        for full in sys.argv[2:]:
            m = repo_meta(full)
            print(json.dumps(m, ensure_ascii=False))
            if m.get("ok"):
                print(json.dumps(tree_count(full, m["branch"]), ensure_ascii=False))
            sys.stdout.flush()
