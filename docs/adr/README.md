# Architecture decision records

An architecture decision record (ADR) captures one decision that shapes FeROS
Sources: what was decided, why, and what follows from it.

## Process

- File name: `NNNN-short-title.md`, numbered in sequence.
- Sections: Status, Context, Decision, Consequences.
- Status is `Proposed`, `Accepted`, `Rejected`, or `Superseded by NNNN`.
- Changes go through a pull request with maintainer approval, like any other file.
- An accepted ADR is not rewritten. To change a decision, add a new ADR that
  supersedes it and update the old one's status line only.

## Index

| ADR                                  | Title                                            | Status   |
|--------------------------------------|--------------------------------------------------|----------|
| [0001](0001-rename-to-sources.md)    | Name the project FeROS Sources                   | Accepted |
| [0002](0002-protect-main.md)         | Protect `main` with validation and code owners   | Accepted |
