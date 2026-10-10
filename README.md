# FeROS Sources

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Format: TOML](https://img.shields.io/badge/Format-TOML-9c4121?style=flat-square)](#catalog-organization)

Versioned sources of supported platforms for the FeROS ecosystem.

A source is what consumers trust and read from. FeROS Sources provides three
layers:

| Layer        | File                                         | Purpose                                       |
|--------------|----------------------------------------------|-----------------------------------------------|
| Repositories | `repository.toml`                            | Registry of recognized official sources       |
| Catalogs     | `catalog.toml`                               | Index of devices, by brand and model          |
| Devices      | `official/<brand>/`, `experimental/<brand>/` | Versioned definition of each supported device |

FeROS Sources identifies supported platforms and describes their execution or
media contracts. Each device has a stable identity and an independent version.
Definitions are organized by support level, brand, and model or variant.

## Catalog organization

| Location                 | Purpose                          |
|--------------------------|----------------------------------|
| `official/qemu/`         | Official QEMU device definitions |
| `experimental/anbernic/` | Experimental Anbernic devices    |
| `experimental/powkiddy/` | Experimental PowKiddy devices    |
| `experimental/trimui/`   | Experimental TrimUI devices      |

This is the agreed catalog structure. Empty categories do not imply that a
manifest or working implementation exists for that brand.

The first designated official device is **FeROS QEMU Virt AArch64 — Cortex-A55**,
with ID `qemu-virt-aarch64-cortex-a55`. Its manifest belongs at
`official/qemu/qemu-virt-aarch64-cortex-a55.toml`. Its initial verification scope
is Core compilation, ELF validation, and boot with the expected `FeROS` UART
output. PowKiddy X55 and Anbernic RG35XX remain experimental for FeROS.

## Responsibilities

| Component | Responsibility                                                   |
|-----------|------------------------------------------------------------------|
| Sources   | Versioned platform definitions and their compatibility contracts |
| Core      | Operating-system and platform implementation                     |
| Builder   | Image construction and validation                                |
| Flasher   | Supported physical-media operations                              |
| Workspace | Selection and orchestration of components                        |

A device only declares applicable operations. QEMU execution does not require
a physical-media flashing contract. Adding a manifest does not implement a new
image format, driver, or device operation in a consumer.

Firmware binaries, system images, ROM collections, and generated build outputs
are outside this repository's distribution scope.

## Versions and support

Device versions, schema versions, and catalog release versions are separate.
Filenames and device IDs remain stable; device versions live inside manifests.
Published revisions are immutable. Promotion from experimental to official
preserves the device ID and requires verification evidence.

Official support covers documented and verified operations. It does not imply
support for every device feature, emulator version, or host OS. See
[VERSIONING.md](VERSIONING.md) and [STABILITY.md](STABILITY.md).

## Consumer integration

The intended integration supports offline operation through an embedded catalog
and a locally retained, validated catalog. Consumers may discover newer device
revisions online, validate their authenticity and compatibility, and activate
them only after successful validation. Failed updates retain the last usable
revision; active operations use a fixed revision.

The catalog schema and update protocol are being defined. This repository does
not yet provide an automatic updater or claim that existing consumers implement
this integration. No catalog release has been published at initialization.

## Contributing

- [Changelog](CHANGELOG.md) and [release procedure](RELEASE.md)
- [Versioning](VERSIONING.md) and [stability](STABILITY.md)
- [Architecture decisions](docs/adr/README.md)
- [Collaborators](COLLABORATORS.md) and [code of conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md) and [third-party components](THIRD_PARTY.md)

Maintained by **Isidro A. López G.**, FeROS Project.

## License

MIT. Copyright (c) 2026 Isidro A. Lopez G. — FeROS::Sources.
See [LICENSE](LICENSE) and [THIRD_PARTY.md](THIRD_PARTY.md).
