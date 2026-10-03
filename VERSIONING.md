# Versioning Policy

FeROS Targets separates target revisions, the manifest schema, and catalog
releases. None follows the version of Core, Builder, Flasher, firmware, or QEMU.

## Target revisions

Each target has a stable ID and its own `MAJOR.MINOR.PATCH` version inside its
manifest. Filenames remain stable. Published revisions are immutable: any
change to a published manifest, including metadata or support status, requires
a new target version. Changes to repository documentation alone do not.

During `0.x`, minor versions may change the operational contract. Patch versions
normally contain compatible corrections or metadata updates. Document any fix
that rejects previously accepted inputs. From `1.0`, major versions indicate
incompatible contract changes, minor versions compatible additions, and patch
versions compatible corrections.

Changing the identity to a different device or variant requires a new ID.
Moving a target from `experimental/<brand>/` to `official/<brand>/` preserves
its ID, increments its version, and requires documented verification evidence.

## Manifest schema

The schema version identifies the structure and semantics a consumer must
understand. Target revision numbers do not indicate schema compatibility.
The new catalog schema is still being defined; the existing X55 manifest's
`manifest_version = 1` belongs to the legacy reader and is not a target release
version. Specify the migration before publishing a replacement schema.

Consumers must reject unsupported schemas and required capabilities. A newer
target version alone does not make an older consumer capable of using it.

## Catalog releases

Catalog tags use `vMAJOR.MINOR.PATCH` and identify complete published snapshots.
A catalog release may update several targets while leaving others unchanged.
Before `1.0`, a minor release may change catalog or schema contracts; a patch
release contains compatible corrections. From `1.0`, incompatible public
contract changes require a major release, compatible additions a minor release,
and compatible corrections a patch release.

Published tags, target revisions, and release assets must not be silently moved
or replaced. Publish a new version to correct an error. Release notes identify
changed target versions, compatibility effects, and verification evidence.
Every CHANGELOG release entry includes its actual publication date; unreleased
work must not be presented as a published release.

The planned update index will associate each target ID and version with its
location and content digest. Consumers should select a newer compatible revision
and retain the last usable local revision if an update fails. Catalog discovery
and authenticated updating remain consumer work, not existing repository features.
