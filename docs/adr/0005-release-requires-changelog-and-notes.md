# 0005: A release requires a dated changelog entry and release notes

Status: Accepted (2026-10-10)

## Context

[VERSIONING.md](../../VERSIONING.md) requires every changelog release entry to
carry its actual publication date and says release notes identify changed
devices, compatibility effects, and verification evidence.
[0004](0004-release-on-version-bump.md) publishes a release automatically when
`catalog_version` is raised, so these requirements need an automatic check.

## Decision

The release pull request contains, besides the version bump:

- a `## [X.Y.Z] - YYYY-MM-DD` entry in `CHANGELOG.md` with a date that is not in
  the future;
- `../../releases`, used as the body of the GitHub Release.

`.github/workflows/release.yml` fails, and publishes nothing, if either is
missing or if the notes still contain the marker `TODO`.

## Consequences

- Placeholders for verification evidence can be committed in advance, but cannot
  be released.
- Release notes are reviewed and approved with the version bump.
- Published notes are not edited afterwards; corrections go in the next release.
