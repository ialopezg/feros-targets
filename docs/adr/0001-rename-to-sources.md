# 0001: Name the project FeROS Sources

Status: Accepted (2026-10-10)

## Context

The project was called FeROS Targets. It holds more than targets: a registry of
official repositories, catalogs of devices, and the device manifests themselves.
"Targets" described only the last layer, and "repositories" or "catalog" described
only one each.

## Decision

The project is **FeROS Sources**. A source defines three layers:

- repositories: `repository.toml`, the registry of recognized official sources;
- catalogs: `catalog.toml`, the index of devices by brand and model;
- devices: `official/<brand>/` and `experimental/<brand>/`, one manifest each.

The thing a manifest describes is called a *device*, not a target.

## Consequences

- File paths, device IDs, and `repository_id` are unchanged, so existing
  consumers and the manifest hash are unaffected.
- The repository URL changes with the repository name. Consumers that match the
  official URL must update their registry (see [repository.md](../repository.md)).
- Documentation uses "device" for what was previously called "target".
