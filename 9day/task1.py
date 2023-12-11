_input = open("in.txt", "rt").read()


def parse_int_line(s: str) -> list[int]:
    return [int(x) for x in s.split(" ") if x != ""]


def rec(nums):
    nums = tuple(s - f for f, s in zip(nums[:-1], nums[1:]))
    if len(set(nums)) != 1:
        val = rec(nums)
        return nums[-1] + val
    return nums[-1]


res = 0
for line in _input.split("\n"):
    nums = parse_int_line(line)
    res += rec(nums) + nums[-1]

print(res)
