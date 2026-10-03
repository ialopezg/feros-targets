# Contributing to FeROS Targets

FeROS Targets owns versioned, declarative target definitions for the FeROS
ecosystem. Core implements the operating system; Builder constructs images;
Flasher handles supported media operations. A manifest describes a contract,
but does not implement new hardware support in those consumers.

## Organization

- `official/<brand>/`: targets maintained under a documented verification contract.
- `experimental/<brand>/`: targets under investigation or with incomplete verification.

QEMU is the first designated official platform. Its initial target is
`official/qemu/qemu-virt-aarch64-cortex-a55.toml`.
PowKiddy X55 and Anbernic RG35XX remain experimental.

Keep stable target IDs and filenames; record each target's version inside its
manifest. Promotion between support levels preserves identity. Use English for
manifests, diagnostics, comments, and documentation.

## Target changes

Explain the target identity, intended consumers, required capabilities, and
evidence for operational values. Distinguish observed behavior from assumptions.
Do not copy addresses, offsets, signatures, or boot settings from another model
without supporting evidence. Keep manifests declarative; do not embed arbitrary
shell commands or executable update hooks.

Version published target changes according to [VERSIONING.md](VERSIONING.md).
Document compatibility effects and any required consumer changes. During the
initial schema design, label proposals as proposals; do not claim that existing
tools already accept them.

## Verification and review

Pull requests must describe the problem, resulting contract, and verification.
Check TOML syntax and, when available, the repository's schema and consumer
validation. Record the commands, tool versions, and results used; do not claim
automated checks exist before they are implemented.

Official support requires reproducible evidence for the declared operations.
For the initial QEMU target this includes building the Core payload, checking
the ELF, and observing the expected UART output during boot. Emulator success
does not establish physical-device support.

Submit minimal synthetic fixtures where possible. Do not commit firmware,
generated images, ROM collections, credentials, or identifiable device dumps.
Preserve third-party notices and submit only material you may distribute under
its applicable license. Original contributions use the repository's MIT license;
no contributor agreement is required.

The maintainer reviews contributions on a best-effort basis. Follow
[SECURITY.md](SECURITY.md) for vulnerabilities and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for participation.
