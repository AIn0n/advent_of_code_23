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


def test_split_first_is_to_the_left():
    """
    |-----|
        |----|
    """

    first = Range(20, 10)
    second = Range.from_str("0 25 10")

    res = first.split(second)

    assert len(res) == 2

    expected = [Range(20, 5), Range(0, 5)]

    assert (expected[0] == res[0] and expected[1] == res[1]) or (
        expected[0] == res[1] and expected[1] == res[0]
    )


def test_split_first_is_shifted_towards_left_edge_case():
    """
    |---|
        |----|
    """

    first = Range(20, 10)
    second = Range.from_str("0 29 10")

    res = first.split(second)

    assert len(res) == 2

    expected = [Range(20, 9), Range(0, 1)]

    assert (expected[0] == res[0] and expected[1] == res[1]) or (
        expected[0] == res[1] and expected[1] == res[0]
    )


def test_split_first_is_shifted_towards_left_edge_case_small_second():
    """
    |----|
        ||
    """

    first = Range(20, 10)
    second = Range.from_str("0 28 2")

    res = first.split(second)

    assert len(res) == 2

    expected = [Range(20, 8), Range(0, 2)]

    assert (expected[0] == res[0] and expected[1] == res[1]) or (
        expected[0] == res[1] and expected[1] == res[0]
    )


def test_split_first_non_overlapping_second_returns_first_with_no_changes():
    """
    |--|
            |---|
    """
    first = Range(20, 10)
    second = Range.from_str("0 30 10")

    res = first.split(second)

    assert res[0] == first

def test_split_first_non_overlapping_second_returns_first_with_no_changes_right_scenario():
    """
            |----|
    |---|
    """
    first = Range(20, 10)
    second = Range.from_str("0 10 10")

    res = first.split(second)

    assert res[0] == first
