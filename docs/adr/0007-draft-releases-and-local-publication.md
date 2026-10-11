# ADR 0007: Draft Releases and Local Publication

- **Status:** Accepted
- **Date:** 2026-10-10

## Context

ADR 0004 established release automation after a catalog version change. ADR 0005 required a changelog and committed release-notes document. Committing temporary release notes duplicates release information and unnecessarily expands repository history. Publication should require deliberate maintainer authorization.

## Decision

1. A version change in `src/catalog.toml` merged to `main` triggers release preparation in GitHub Actions.
2. The workflow validates the repository and dated `CHANGELOG.md` entry, builds deterministic assets, and creates a **draft** GitHub Release with generated starter notes.
3. Maintainers review and edit release notes in the GitHub draft. No separate release-notes Markdown file is committed.
4. Local `make release-status` inspects the draft; `make release-publish` verifies the current version, branch, remote main, local tag, draft state, nonempty reviewed notes, and expected asset names, then requests explicit confirmation before publication.
5. Publishing an existing draft does not create commits, move tags, rebuild assets, or modify source manifests.
6. This decision supersedes the committed release-notes-file requirement of ADR 0005, but retains its changelog requirement. It refines the automatic-publication behavior of ADR 0004 into automatic draft preparation.

## Consequences

- GitHub Releases own release-specific narrative; `CHANGELOG.md` remains the tracked version history.
- Publication requires GitHub CLI authentication and local GNU Make / Python tooling.
- A draft may be edited without further Git commits.
- Asset integrity and permissions remain the responsibility of the workflow and GitHub release configuration.
