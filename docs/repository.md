# Repository registry

`repository.toml` is the registry of repositories that FeROS Sources recognizes
as official sources. It answers one question: *which sources are trusted as
official?* It does not list devices; catalogs and device manifests do. See
[catalog.md](catalog.md) and [device.md](device.md).

## Format

```toml
schema_version = 1

[[repositories]]
name = "FeROS Official Repository"
url = "https://github.com/ialopezg/feros-sources"
published_date = "2026-10-04T01:49:59Z"
```

| Field            | Meaning                                                      |
|------------------|--------------------------------------------------------------|
| `schema_version` | Integer version of this registry format. Currently `1`.      |
| `name`           | Display name of the repository.                              |
| `url`            | Identity of the source. Not a download endpoint.             |
| `published_date` | Informational timestamp. It is not proof of authenticity.    |

The registry uses its own integer schema version. It is independent of the
catalog and manifest contract (`schema_version = "1.0"`).

## Rules

- `url` identifies a source; it never tells a consumer where to download from.
  Acquisition of catalogs and manifests is defined in [catalog.md](catalog.md).
- A remote catalog cannot grant itself official status. Its `repository_id`
  names its source but does not authenticate it. Official status comes only
  from a registry the consumer configured independently.
- Each URL appears once. The validation script rejects duplicates and URLs that
  are not under `https://github.com/`.
- Adding, removing, or changing an entry changes who is trusted. It receives the
  same review as a manifest, and a changed `url` changes the source's identity,
  so consumers that matched the old URL must update their registry.

## Not covered

This file is not a consumer's local subscription store, and it does not define
an update protocol or signature verification. Those remain consumer work, as
stated in [SECURITY.md](../SECURITY.md).
