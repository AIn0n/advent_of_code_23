from task1 import solution

def test_single_op():
    assert solution(["L50"]) == 1

def test_large_negative_move():
    assert solution(["L250"]) == 1

def test_example_input():
    assert solution([
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]) == 3

def test_on_valid_input_greater_than_986():
    assert solution(open("valid_input.txt").readlines()) > 986