# Stability Policy

FeROS Targets is establishing its initial catalog and manifest contract.
No catalog release has been published at initialization.

| Area                 | Commitment                                                                                                         |
|----------------------|--------------------------------------------------------------------------------------------------------------------|
| Identity             | Stable IDs across revisions and support-level changes                                                              |
| Target version       | Independent version for each published target definition                                                           |
| Schema               | Versioned contract; unsupported schemas must be rejected                                                           |
| Official targets     | Documented scope and reproducible verification evidence                                                            |
| Experimental targets | Incomplete or evolving support, with explicit limitations                                                          |
| Consumers            | A definition only enables operations the consumer implements                                                       |
| Updates              | Offline operation and validated local updates are design requirements, not implemented features of this repository |

The first designated official target is
`qemu-virt-aarch64-cortex-a55`: QEMU `virt`, Cortex-A55, AArch64, ELF loading
through `-kernel`, and UART output. Its initial verification contract covers
Core compilation, ELF checks, and observed `FeROS` serial output. Record the
tested QEMU and toolchain versions before publishing its definition.

PowKiddy X55 and Anbernic RG35XX remain experimental. Booting vendor software
does not verify FeROS boot on either device.

Official support describes the target's declared operations, not every hardware
feature, QEMU version, or host operating system. Host support belongs to each
consumer's tested matrix. The catalog itself does not distribute native binaries.

There is no LTS or availability SLA. See [VERSIONING.md](VERSIONING.md) for
compatibility and [SECURITY.md](SECURITY.md) for security maintenance.
