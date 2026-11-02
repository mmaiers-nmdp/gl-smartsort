"""Smart sort a GL String.

As of this version, gl-smartsort is a thin wrapper over the standards-conformant
`glstring` library (https://pypi.org/project/glstring/). Sorting is performed on
`glstring`'s parsed GL String 1.1 AST rather than by recursive string splitting.

Historical behaviour (the original `SmartSort.pm`, 2012, Martin J. Maiers) is
preserved by delegating to ``glstring.smart_sort(gl, legacy=True)``:

- Recursive ordering across delimiter levels ``^ | + ~ /``.
- Ordering primarily by gene/locus (left of ``*``), then **numerically** by
  allele fields, so ``A*01:11`` precedes ``A*01:103``.
- In legacy mode, ``~`` phased groups and ``+`` gene copies are reordered, as in
  the original comparator.

The AST-based implementation is more correct than the previous string-splitting
port in several edge cases (deterministic expression-suffix tie-breaking,
variable-width numeric fields, precedence correctness on mixed-operator strings,
and GL String 1.1 ``?`` support). See CHANGELOG for the behavioural notes.

Example:
    smart_sort("A*01:103+A*01:11") -> "A*01:11+A*01:103"
"""

from __future__ import annotations

from glstring import smart_sort as _glstring_smart_sort

__all__ = ["smart_sort"]


def smart_sort(glstring: str) -> str:
    """Canonicalize a GL String by smart (numeric, locus-aware) sorting.

    Delegates to :func:`glstring.smart_sort` in ``legacy=True`` mode, which
    reproduces the historical gl-smartsort / ``SmartSort.pm`` ordering
    convention (including reordering of ``~`` and ``+`` levels).

    Parameters
    ----------
    glstring:
        A GL String (GL String 1.0 or 1.1).

    Returns
    -------
    str
        The smart-sorted GL String.
    """
    return _glstring_smart_sort(glstring, legacy=True)
