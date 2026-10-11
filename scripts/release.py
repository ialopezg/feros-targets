#!/usr/bin/env python3
"""Inspect and publish an existing GitHub draft. Never create tags or assets."""
import json
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(*args):
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"status", "publish"}:
        print("Usage: python scripts/release.py {status|publish}", file=sys.stderr)
        return 2
    version = tomllib.loads((ROOT / "src/catalog.toml").read_text(encoding="utf-8"))["catalog_version"]
    tag = f"v{version}"
    try:
        release = json.loads(run("gh", "release", "view", tag, "--json", "tagName,isDraft,isPrerelease,targetCommitish,body,assets,url"))
        branch = run("git", "branch", "--show-current")
        head = run("git", "rev-parse", "HEAD")
        remote_head = run("git", "ls-remote", "origin", "refs/heads/main").split()[0]
        tag_commit = run("git", "rev-list", "-n", "1", tag)
    except (OSError, subprocess.CalledProcessError, IndexError, ValueError) as exc:
        print(f"Unable to verify release: {exc}", file=sys.stderr)
        return 1
    print(f"Release: {tag} | Draft: {release['isDraft']} | URL: {release['url']}")
    if sys.argv[1] == "status":
        return 0
    assets = {a["name"] for a in release["assets"]}
    expected = {f"feros-sources-{tag}.tar.gz", "SHA256SUMS"}
    if (branch != "main" or head != remote_head or head != tag_commit
            or not release["isDraft"] or release["isPrerelease"]
            or not release["body"].strip() or "TODO" in release["body"]
            or not expected.issubset(assets)):
        print("Publication blocked: verify main, origin/main, tag, draft notes and assets.", file=sys.stderr)
        return 1
    if input(f"Publish {tag} at {head[:12]}? Type {tag} to confirm: ").strip() != tag:
        print("Cancelled")
        return 1
    subprocess.run(["gh", "release", "edit", tag, "--draft=false"], cwd=ROOT, check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
