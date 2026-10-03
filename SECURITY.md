# Security Policy

## Private reporting

The planned repository is `ialopezg/feros-targets`. No remote repository or
private vulnerability-reporting channel has been confirmed at initialization.
The maintainer must establish and verify a private channel before the first
public release, then update this section with its address.

Until then, request a private contact without publishing vulnerability details.
Do not disclose credentials, personal data, proprietary firmware, or sensitive
device dumps in public reports. No bounty or response deadline is promised.

Include the target ID and version, catalog commit or release, consumer version,
affected operation, expected impact, and a minimal reproduction.

## Maintenance

No catalog release has been published at initialization. After release, fixes
will target `main` and the latest published catalog. Corrected targets receive
new versions; older revisions receive no routine backports. Document affected
revisions and required consumer upgrades in release notes.

## Trust boundaries

Manifests may influence image acceptance, boot configuration, and media writes.
A parseable manifest or a matching byte marker does not prove image authenticity,
hardware compatibility, or successful boot. Consumers must validate required
fields, supported operations, sizes, and offsets before acting on a definition.

The planned update mechanism must validate publisher authenticity, integrity,
schema support, and required consumer capabilities before activating downloaded
definitions. A checksum alone does not authenticate the publisher. Invalid or
incompatible updates must leave the last usable catalog intact. Each active
operation must keep a fixed target revision.

These are requirements for consumer implementations, not claims that this
repository already provides an updater, signature verification, or a cache.
The catalog contains declarative data, not remotely executable scripts.

## Publication

Review changes to manifests and any validation or publication tooling. Publish
immutable target revisions and catalog releases. Do not silently replace a
published definition. Record the source revision and available verification
evidence. Do not claim signed releases or provenance attestations until those
mechanisms are implemented and verified.
