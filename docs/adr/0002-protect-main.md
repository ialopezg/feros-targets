# 0002: Protect `main` with validation and code owners

Status: Accepted (2026-10-10)

## Context

Manifests can influence image acceptance, boot configuration, and media writes
(see [SECURITY.md](../../SECURITY.md)). Unreviewed or unapproved additions are a
trust risk, and published revisions must stay immutable.

## Decision

- `.github/CODEOWNERS` requires maintainer review for every path.
- `scripts/validate.py` runs in CI as the required `validate` check. It rejects
  files outside the approved layout, binaries, executables, symlinks, non-LF
  line endings, unlisted manifests, catalog mismatches, and executable-style keys.
- Rulesets in `.github/rulesets/` require pull requests, code owner review, and
  the `validate` check on `main`, and protect `v*` tags from being moved or deleted.
- A catalog entry carries the SHA-256 of its manifest, so any change to a
  published manifest is visible and needs a new version.

## Consequences

- Every device addition is one pull request: manifest plus catalog entry.
- The rulesets take effect only after they are imported in the repository settings.
- A solo maintainer needs the admin bypass for pull requests, because GitHub does
  not let an author approve their own pull request. Remove it when a second
  reviewer exists.
