# 0004: Publish a release when `catalog_version` is raised

Status: Accepted (2026-10-10)

## Context

Approved devices land on `main` one pull request at a time. Releases must be
complete, immutable snapshots ([VERSIONING.md](../../VERSIONING.md)), and the
catalog version describes the whole snapshot, not a single device.

## Decision

- Approving a device does not change `catalog_version`. Merged devices wait on
  `main` for the next release.
- A release is a pull request that raises `catalog_version` in `catalog.toml`.
  It follows the same review and `validate` check as every other change.
- When that change lands on `main` and no tag `v<catalog_version>` exists,
  `.github/workflows/release.yml` validates the tree, builds the assets, and
  creates the tag and the GitHub Release at that commit.
- The version must be `MAJOR.MINOR.PATCH` and greater than the latest tag.
  An existing tag is never moved, replaced, or recreated.
- Assets are a reproducible archive of `repository.toml`, `catalog.toml`, the
  listed manifests and `site.json`, plus `SHA256SUMS`.

## Consequences

- The release is triggered by an approved change. Nothing publishes without the
  maintainer approving that version bump.
- `main` can be ahead of the latest release. The site ([0003](0003-publish-latest-main-site.md))
  shows `main`; the release shows the immutable snapshot.
- `SHA256SUMS` detects change but does not authenticate the publisher. No signing
  or provenance attestation is claimed until one is implemented.
- To release, the maintainer raises the version; to correct an error, raises it
  again. Published tags are never edited.
