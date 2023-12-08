from ranges import Range
from pytest import mark


def test_constructor_start_end_len_parameters():
    r = Range(79, 14)

    assert r.start == 79
    assert r._len == 14
    assert r.end == 92


def test_build_from_string_returns_proper_range():
    r = Range.from_str("45 77 23")
    assert r.start == 77
    assert r.shift == (45 - 77)
    assert r._len == 23


def test_split_first_is_smaller_both_sides_returns_shifted_first_range():
    first = Range(79, 14)
    second = Range.from_str("52 50 48")
    res = first.split(second)[0]

    shift = 52 - 50
    assert res.start == first.start + shift
    assert res.end == first.end + shift
    assert res._len == first._len


def test_split_example_from_side():
    first = Range(98, 2)

    assert first.end == 99

    second = Range.from_str("50 98 2")

    res = first.split(second)[0]

    assert res.start == 50
    assert res.end == 51
    assert res._len == 2
