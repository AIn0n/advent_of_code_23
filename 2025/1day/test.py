from task1 import solution
from task2 import solution2

TEST_INPUT = [
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
]
VALID_INPUT = open("valid_input.txt").readlines()

def test_single_op():
    assert solution(["L50"]) == 1

def test_large_negative_move():
    assert solution(["L250"]) == 1

def test_example_input():
    assert solution(TEST_INPUT) == 3

def test_on_valid_input_greater_than_986():
    assert solution(VALID_INPUT) > 986

def test_2_on_test_input():
    assert solution2(TEST_INPUT) == 6

def test_2_on_valid_input_greater_than_4444():
    assert solution2(VALID_INPUT) > 4444

def test_2_given_dial_two_times_pointing_at_zero():
    assert solution2(["L160"]) == 2

def test_2_on_valid_input_lower_than_6442():
    assert solution2(VALID_INPUT) < 6442

def test_2_given_dial_two_times_pointing_at_zero_during_inc():
    assert solution2(["R160"]) == 2

def test_2_given_dial_on_zero_moving_left_returns_one_click():
    assert solution2([
        "L50",  # set dial on zero, should count as one click
        "L5",   # move dial back 5, to 95, shouldn't be counted as one
    ]) == 1