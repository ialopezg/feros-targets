# Device catalog contract 1.0

This candidate defines discovery metadata for Builder. It does not implement
repository updates, device installation, or a new image format. No release or
publication date is asserted by these files.

## Files and identity

- `repository.toml` remains the registry of recognized official repositories.
- `catalog.toml` is the device index published by one repository.
- A device manifest holds that device's versioned definition.

The initial QEMU manifest retains the path and ID documented in README.md.
Brand and model are separate fields; Cortex-A55 identifies the CPU variant.
The catalog has one entry per device ID and advertises one current revision.

`repository_id` identifies the source but does not authenticate it. A remote
file cannot grant itself official status. Repository classification continues
to come from the independently configured official registry. Device `support`
is a separate publisher-declared classification (`official` or `experimental`).

## Versions

- `schema_version = "1.0"` identifies this file contract, independently of
  Builder, the local subscription store and the official repository registry.
- `catalog_version` uses MAJOR.MINOR.PATCH for the complete catalog snapshot.
- Device `version` uses MAJOR.MINOR.PATCH for the individual manifest.
- Device IDs and manifest filenames remain stable across revisions.

Initial consumers accept schema 1.0 explicitly. A new minor schema requires a
compatibility decision; it is not automatically accepted. Breaking changes
require a new major schema. Schema changes never authorize deleting local data.
Published device revisions and catalog snapshots must remain immutable; use a
new version for changes. No timestamps are used as proof of authenticity.

## Fields and validation

Every device entry requires the metadata shown in the initial QEMU manifest.
`kind` is `virtual` or `physical`; `support` is `official` or `experimental`.
`installable` is a boolean. The initial definition requires it to be false:
installation recipes and their compatibility contract are not yet defined.
An empty catalog is represented by `devices = []`. Duplicate device IDs in one
catalog are invalid. Identical IDs in different repositories remain distinct
sources; installation must resolve the source explicitly if ambiguous.

The index also requires `manifest`, a relative POSIX path within the same
repository snapshot, and `sha256`, the 64 lowercase hexadecimal digits of the
manifest's exact bytes. Reject absolute paths, URLs, backslashes and parent
traversal. Index metadata must match the manifest's device table.

SHA-256 detects changed content; it is not a publisher signature. Acquisition
must retain the configured source and a consistent snapshot. For GitHub,
resolve a commit and fetch the catalog and manifests at that same commit.
Repository identity URLs are not catalog download endpoints. Generic endpoint
discovery and authenticated update policy remain a separate implementation step.

## Consumer behavior

`builder repository --update [<index|name>]` will download and validate a
catalog snapshot, then replace its local cache atomically. An error retains the
previous cache. `--info <index|name>` reads one cached catalog; `--search <text>`
searches cached IDs, brands, models and display names case-insensitively across
registered repositories. Results always identify the source and device version.
If no cache exists, show that an update is required; do not report an empty
repository or silently access the network.

`device install` must reject this metadata-only manifest as not installable.
A later recipe will declare prerequisites and verification details. A manifest
alone does not provide a Builder implementation.

## Initial QEMU scope

QEMU is the first designated official device. Existing project policy limits
its intended verified scope to Core compilation, ELF validation and the FeROS
UART boot message. This manifest does not add physical-media operations or
claim an installed toolchain. Record tested Core, QEMU and toolchain revisions
as required by STABILITY.md before publishing an official device release.

This is a new discovery contract, not a reinterpretation of the legacy X55
`manifest_version = 1` RKNS format. Legacy manifests are not indexed until an
explicit migration preserves their image and media contracts.
