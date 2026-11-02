# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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

No functional changes were made to the sorting algorithm.
