# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.0] - 2026-11-02

### Changed

- Refactored the sorting implementation to delegate to the standards-conformant
  [`glstring`](https://pypi.org/project/glstring/) library. `smart_sort` now
  operates on `glstring`'s parsed GL String 1.1 AST instead of recursive string
  splitting. The public API (`smart_sort(gl) -> str`) and the CLI are unchanged.
- `smart_sort` delegates to `glstring.smart_sort(gl, legacy=True)`, which
  preserves the historical `SmartSort.pm` ordering convention (including
  reordering of `~` phased groups and `+` gene copies).

### Added

- `glstring>=0.1.0` runtime dependency.
- Support for the GL String 1.1 `?` (possible gene locations) delimiter, which
  the previous string-splitting implementation could not handle.

### Fixed

- Expression-suffix ordering is now deterministic. The previous implementation
  stripped suffixes before comparison, so e.g. `A*01:01` and `A*01:01N` compared
  equal and their relative order depended on input order. The AST-based
  comparator breaks such ties deterministically by the full allele token.
- Mixed-operator strings are now ordered by correct GL String precedence rather
  than by a first-match delimiter scan.

### Behavioural notes

Output is unchanged for all previously documented test cases. Outputs may differ
from 0.1.x only in the edge cases listed under *Fixed* above (ambiguous suffix
ties, certain mixed-operator strings) and for inputs using the new `?`
delimiter. Numeric allele fields are now compared at full, variable width rather
than being capped at four fields.

### Requirements

- Minimum Python raised to 3.12 (matching `glstring`).

## [0.1.2] - 2026-11-02

### Changed

- Reconciled inconsistent licensing declarations and relicensed the project to
  the Apache License, Version 2.0 (Apache-2.0). Previously, the repository
  contained contradictory declarations: the `LICENSE` file carried the GNU
  General Public License v3, while `pyproject.toml` and `README.md` declared
  MIT. A provenance and contributor review confirmed a single copyright holder
  (Martin J. Maiers, NMDP) with no third-party code, establishing clear
  authority to relicense.
- Replaced the `LICENSE` file with the complete, unmodified Apache-2.0 text and
  added the appropriate copyright attribution.
- Added a `NOTICE` file documenting attribution and the provenance of the
  original `SmartSort.pm` implementation.
- Updated `pyproject.toml` to declare `Apache-2.0` using PEP 639 metadata
  (SPDX license expression and `license-files`), and removed the obsolete MIT
  classifier.
- Updated `README.md` license references and added a provenance note.

This is the first release published to PyPI, and its package metadata
declares Apache-2.0.

No functional changes were made to the sorting algorithm.
