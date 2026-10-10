# Device manifest

A device manifest is the versioned definition of one supported device. It is the
lowest layer of a source: [repository.toml](repository.md) says which sources are
official, [catalog.toml](catalog.md) indexes devices, and the manifest defines
each one.

A manifest is declarative metadata. Adding one does not implement an image
format, a driver, or a device operation in Core, Builder, or Flasher.

## Location and identity

- Path: `official/<brand>/<id>.toml` or `experimental/<brand>/<id>.toml`.
- The directory under the top level equals the device's `brand`.
- The top-level directory equals its `support` level.
- The filename is `<id>.toml`. IDs and filenames stay stable across revisions.
- An ID is lowercase alphanumeric words separated by hyphens.
- A different device or variant needs a new ID.

## Format

```toml
schema_version = "1.0"

[device]
id = "qemu-virt-aarch64-cortex-a55"
name = "FeROS QEMU Virt AArch64 — Cortex-A55"
brand = "qemu"
model = "virt"
architecture = "aarch64"
cpu = "cortex-a55"
kind = "virtual"
version = "0.1.0"
support = "official"
installable = false
```

| Field          | Rule                                                          |
|----------------|---------------------------------------------------------------|
| `id`           | Stable identity, unique within a catalog.                     |
| `name`         | Display name.                                                 |
| `brand`        | Brand or platform. Matches the directory.                     |
| `model`        | Model of the brand. Separate from `cpu`.                      |
| `architecture` | Instruction set architecture.                                 |
| `cpu`          | CPU variant.                                                  |
| `kind`         | `virtual` or `physical`.                                      |
| `version`      | `MAJOR.MINOR.PATCH` of this manifest.                         |
| `support`      | `official` or `experimental`. Matches the top-level directory.|
| `installable`  | Boolean. Must be `false` under contract 1.0.                  |

Every field must also match the device's entry in `catalog.toml`.

## Versions and immutability

A published manifest never changes silently. Any change, including metadata or
the support level, needs a new `version` and a new `sha256` in `catalog.toml`.
Promotion from `experimental/` to `official/` keeps the ID, raises the version,
and needs verification evidence as described in [STABILITY.md](../STABILITY.md)
and [VERSIONING.md](../VERSIONING.md).

## What a manifest must not contain

- Executable content: no shell commands, scripts, or hooks. The validation script
  rejects keys such as `command`, `exec`, `script`, `hook`, and `run`.
- Values copied from another model without evidence (addresses, offsets,
  signatures, boot settings). Distinguish observed behavior from assumptions.
- Firmware, images, ROMs, credentials, or identifiable device dumps.

## Adding a device

One pull request containing:

1. The manifest at its approved path.
2. Its entry in `catalog.toml`, with the manifest's SHA-256.
3. The description and evidence required by [CONTRIBUTING.md](../CONTRIBUTING.md).

`python scripts/validate.py` must pass, and the maintainer must approve.

## Legacy manifests

The earlier PowKiddy X55 format (`manifest_version = 1`) is a different contract.
Legacy manifests are not indexed until a migration preserves their image and
media contracts.
