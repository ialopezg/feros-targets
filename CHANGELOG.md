# Changelog

All notable changes to FeROS Sources are recorded here. Entries describe catalog
releases, which are versioned as described in [VERSIONING.md](VERSIONING.md).
Every release entry carries its actual publication date; unreleased work is
listed under Unreleased and is not a published release.

## [0.1.0] - 2026-10-10

Work planned for the first release, `0.1.0`. Nothing has been published yet.
When releasing, rename this heading to `## [0.1.0] - YYYY-MM-DD` using the real
date, and start a new empty Unreleased section above it.

### Added

- Catalog layout: `official/<brand>/` and `experimental/<brand>/`.
- Device catalog contract 1.0 (candidate), documented in
  [docs/catalog.md](docs/catalog.md), with the repository registry in
  [docs/repository.md](docs/repository.md) and the manifest format in
  [docs/device.md](docs/device.md).
- `repository.toml`, the registry of recognized official sources.
- `catalog.toml` at catalog version `0.1.0`, with one entry per device and the
  SHA-256 of each manifest.
- Device `qemu-virt-aarch64-cortex-a55` at version `0.1.0`: QEMU `virt`,
  Cortex-A55, AArch64. Official, virtual, not installable.
- Project policies: contributing, code of conduct, security, stability,
  versioning, third-party material, and collaborators.
- Architecture decision records in [docs/adr/](docs/adr/README.md).
- Validation script `scripts/validate.py`, run in CI as the `validate` check.
- Repository protection: `CODEOWNERS` and rulesets for `main` and `v*` tags.
- Static site published from `main` through GitHub Pages.
- Release workflow that publishes a release when `catalog_version` is raised.
