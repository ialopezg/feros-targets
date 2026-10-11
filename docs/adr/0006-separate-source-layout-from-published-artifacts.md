# ADR 0006: Separate Source Layout from Published Artifacts

- **Status:** Accepted
- **Date:** 2026-10-10

## Context

FeROS Sources stores repository metadata, a device catalog, and approved device manifests as TOML files. The catalog's `manifest` entries are paths relative to the published catalog root. The current repository also uses that same root as the source directory, mixing distributable data with project governance, documentation, and tooling.

The site publishes the latest approved state of `main`; it is not itself a versioned release. Device manifest checksums in `catalog.toml` are calculated from the exact manifest bytes.

## Decision

1. Store authoritative TOML files under `src/`: `src/repository.toml`, `src/catalog.toml`, and `src/{official,experimental}/<brand>/<device>.toml`.
2. Keep catalog `manifest` values **relative to `src/`**, without a `src/` prefix. Their values and published URLs remain unchanged.
3. Keep validation and generation utilities under `scripts/`; reserve `site/` for optional website-only templates and assets. Project documentation remains under `docs/` and standard repository governance files remain at the repository root.
4. Build the public site into `dist/site/`, mapping files from `src/` directly to the output root: `src/catalog.toml` becomes `dist/site/catalog.toml`.
5. Publish only `repository.toml`, `catalog.toml`, and manifests explicitly listed in the catalog, plus generated site metadata and presentation files. Do not publish arbitrary files from `src/`.
6. Copy TOML files byte-for-byte. Validate catalog checksums against source manifests before building; preserve the same bytes in published artifacts.
7. Exclude `dist/` from version control. GitHub Pages deploys generated output rather than committing it to `main`.
8. Preserve the catalog schema, relative manifest contract, and release/versioning rules. A source-directory relocation alone does not require a catalog version bump.

## Consequences

- Repository structure is independent from the public catalog layout.
- Consumers such as FeROS Builder continue resolving manifests relative to the catalog URL without learning the internal `src/` directory.
- Validator and site builder resolve local source paths using `src/`, while published links omit that prefix.
- CI workflows and documentation referencing the old repository-root TOML locations must be updated as part of the migration.
- Build artifacts can be regenerated deterministically from an approved checkout.

## Migration

1. Move existing TOML files into `src/` with `git mv`, preserving their bytes.
2. Update `scripts/validate.py`, `scripts/build_site.py`, and the Pages workflow to use the new directories.
3. Update repository documentation and any workflow path filters that reference root TOML files.
4. Stage all files, run validation, build the site, and verify the published manifest checksums and relative links before committing.

## Alternatives considered

- **Keep TOML files at the repository root:** simpler initially, but couples source organization to the publication contract.
- **Publish `src/` as part of public URLs:** exposes internal layout to consumers and unnecessarily changes the catalog contract.
- **Commit generated site output:** duplicates derived data in version control and increases the risk of stale publication artifacts.
