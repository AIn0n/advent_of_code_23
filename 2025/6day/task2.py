from operator import add, mul
from functools import reduce
from string import whitespace

OP = {
    "+": add,
    "*": mul
}

INIT = {
    "+": 0,
    "*": 1,
}

def solution(rows: list[str]) -> int:
    curr_op = " "
    num_stack = []
    res = 0
    for col in range(len(rows[0])):
        cell = [row[col] for row in rows]
        if cell[-1] not in whitespace:
            curr_op = cell[-1]
        if all(el in whitespace for el in cell):
            res += reduce(lambda x, y: OP[curr_op](x, y), num_stack, INIT[curr_op])
            num_stack.clear()
            continue
        num_stack.append(int("".join(cell[:-1])))


    return res


if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))