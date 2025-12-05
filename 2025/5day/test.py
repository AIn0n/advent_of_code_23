from task2 import solution as s2

def test_second_task_answer_is_lower_than_n():
    assert s2(open("valid_input.txt").readlines()) < 442936863489814