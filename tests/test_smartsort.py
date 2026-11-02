from gl_smartsort import smart_sort


# -- Backward-compatible behaviour (unchanged outputs vs the 0.1.x port) -----


def test_basic_numeric_order():
    assert smart_sort("A*01:103+A*01:11") == "A*01:11+A*01:103"


def test_locus_ordering_blocks():
    assert smart_sort("B*07:02^A*02:01") == "A*02:01^B*07:02"


def test_suffix_tie_break():
    # Numeric fields equal; the expression suffix now breaks the tie
    # deterministically (previously suffix-stripping left this input-order
    # dependent). Output is unchanged for this case.
    assert smart_sort("A*01:01N+A*01:01") == "A*01:01+A*01:01N"


def test_nested_delims():
    # + inside ^
    assert smart_sort("A*02:01+A*01:01^B*08:01+B*07:02") == "A*01:01+A*02:01^B*07:02+B*08:01"


# -- New behaviour available via the glstring-backed implementation ----------


def test_numeric_not_lexical_variable_width():
    assert smart_sort("A*01:11/A*01:103/A*01:02") == "A*01:02/A*01:11/A*01:103"


def test_idempotent():
    for s in (
        "A*01:103+A*01:11",
        "B*07:02^A*02:01",
        "A*02:01+A*01:01^B*08:01+B*07:02",
    ):
        once = smart_sort(s)
        assert smart_sort(once) == once


def test_input_order_independence():
    assert smart_sort("A*02:01/A*01:01") == smart_sort("A*01:01/A*02:01")


def test_gl_string_1_1_possible_locus():
    # '?' (GL String 1.1) was unsupported by the previous string-splitting
    # implementation; it now parses and sorts correctly.
    out = smart_sort("KIR2DL5B*00201?KIR2DL5A*00501")
    assert "?" in out
    assert out == "KIR2DL5A*00501?KIR2DL5B*00201"
