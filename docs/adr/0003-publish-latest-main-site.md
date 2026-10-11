# 0003: Publish the latest `main` as a static site

Status: Accepted (2026-10-10)

## Context

Consumers and people need a stable web address for the current sources. The
project documents that repository URLs identify sources and are not catalog
download endpoints, and that a catalog and its manifests must come from one
consistent snapshot ([catalog.md](../catalog.md)).

## Decision

- GitHub Pages publishes `https://ialopezg.github.io/feros-sources`, deployed by
  `.github/workflows/pages.yml` on every push to `main`.
- The workflow validates the tree, then `scripts/build_site.py` builds `_site/`
  from that single commit: `repository.toml`, `catalog.toml`, the manifests the
  catalog lists, `site.json`, and an index page.
- `site.json` records the commit and the SHA-256 of every published file.
- The site shows the latest approved state of `main`. It is not a release.
  Immutable releases remain separate (tags and release assets).
- Only manifests listed in `catalog.toml` are published.

## Consequences

- The site's content changes with every merge. Consumers that need a fixed
  revision must pin the commit from `site.json` or use a release.
- The site address is a publication location. It does not replace the
  repository URL in `repository.toml` as the source identity, and it grants no
  official status.
- A checksum detects change but does not authenticate the publisher. No signing
  is claimed.
- Pages must be enabled with GitHub Actions as the source (repository settings).
