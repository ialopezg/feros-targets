# Contributing to FeROS Sources

FeROS Sources owns versioned, declarative device definitions for the FeROS
ecosystem. Core implements the operating system; Builder constructs images;
Flasher handles supported media operations. A manifest describes a contract,
but does not implement new hardware support in those consumers.

## Organization

- `official/<brand>/`: devices maintained under a documented verification contract.
- `experimental/<brand>/`: devices under investigation or with incomplete verification.

QEMU is the first designated official platform. Its initial device is
`official/qemu/qemu-virt-aarch64-cortex-a55.toml`.
PowKiddy X55 and Anbernic RG35XX remain experimental.

Keep stable device IDs and filenames; record each device's version inside its
manifest. Promotion between support levels preserves identity. Use English for
manifests, diagnostics, comments, and documentation.

## Device changes

Explain the device identity, intended consumers, required capabilities, and
evidence for operational values. Distinguish observed behavior from assumptions.
Do not copy addresses, offsets, signatures, or boot settings from another model
without supporting evidence. Keep manifests declarative; do not embed arbitrary
shell commands or executable update hooks.

Version published device changes according to [VERSIONING.md](VERSIONING.md).
Document compatibility effects and any required consumer changes. During the
initial schema design, label proposals as proposals; do not claim that existing
tools already accept them.

## Verification and review

Pull requests must describe the problem, resulting contract, and verification.
Check TOML syntax and, when available, the repository's schema and consumer
validation. Record the commands, tool versions, and results used; do not claim
automated checks exist before they are implemented.

Official support requires reproducible evidence for the declared operations.
For the initial QEMU device this includes building the Core payload, checking
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

## Approval and protection

Nothing reaches `main` without maintainer approval. Changes arrive through pull
requests, require review from the code owner in `.github/CODEOWNERS`, and must
pass the `validate` check (`python scripts/validate.py`, Python 3.11 or later).

The check rejects files outside the approved layout, binaries, executables,
symlinks, non-LF line endings, manifests not listed in `catalog.toml`, catalog
entries whose SHA-256, path, ID, brand, or support level do not match their
manifest, and executable-style keys in manifests. Adding a device therefore
means adding its manifest and its catalog entry in the same pull request.
Changing a published manifest means a new device version and an updated hash.

Changes to `scripts/`, `.github/`, `repository.toml`, and `LICENSE` receive the
same review as manifests. Repository rulesets are in `.github/rulesets/`.

