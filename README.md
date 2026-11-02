# gl-smartsort

A tiny Python package that canonicalizes **GL Strings** by *smart sorting*:
- recursively sorts within delimiter levels in precedence: `^`, `|`, `+`, `~`, `/`
- orders blocks by **gene/locus** (left of `*`)
- orders alleles **numerically** (not lexically) within a locus (e.g., `A*01:11` before `A*01:103`)
- strips suffixes for numeric comparison (e.g., `01:01N` compares as `01:01`)

This is a Python port of `SmartSort.pm` (2012-11-14).

## Install (local)

From the project directory:

```bash
python -m pip install -U pip
python -m pip install -e .
```

## Usage (Python)

```python
from gl_smartsort import smart_sort

print(smart_sort("A*01:103+A*01:11"))
# A*01:11+A*01:103
```

## Usage (CLI)

Sort a single GL string:

```bash
gl-smartsort "B*07:02^A*02:01"
```

Or sort from stdin (one per line):

```bash
cat gl.txt | gl-smartsort
```

## Provenance

This package is a Python port of the original Perl implementation
`SmartSort.pm` (2012-11-14), authored by Martin J. Maiers. Both the original
Perl implementation and this Python port were written by the same author. The
implementation relies only on the Python standard library and incorporates no
third-party source code.

## License

Licensed under the Apache License, Version 2.0 (Apache-2.0). See the
[LICENSE](LICENSE) and [NOTICE](NOTICE) files for details.

Copyright 2012 Martin J. Maiers and National Marrow Donor Program (NMDP).

