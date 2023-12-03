from typing import Optional
from functools import reduce
from operator import mul

_input = open("in.txt", "rt").read()

lines = [f"_{x}_" for x in _input.split("\n")]
empty_line = "_" * len(lines[0])
lines = [empty_line, *lines, empty_line]


def parse_num(s: str, ptr: int) -> Optional[int]:
    res = ""
    if not s[ptr].isdigit():
        return None
    # parse to left
    for i in range(ptr - 1, -1, -1):
        if not s[i].isdigit():
            break
        res = s[i] + res

    # parse to right
    for c in s[ptr:]:
        if not c.isdigit():
            break
        res += c
    return int(res) if len(res) else None


res = 0

pairs = []
for row in range(-1, 2):
    for col in range(-1, 2):
        if row or col:
            pairs.append(tuple([row, col]))

for i in range(len(lines)):
    for j in range(len(lines[i])):
        c = lines[i][j]
        if c == "*":
            nums = set(parse_num(lines[i + row], j + col) for row, col in pairs)
            nums.remove(None)
            if len(nums) == 2:
                res += reduce(mul, nums, 1)

print(res)
