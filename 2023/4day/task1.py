_input = open("in.txt", "rt").read()


def parse_int_line(s: str) -> set[int]:
    return set([int(x) for x in s.split(" ") if x != ""])


def count_points(n: int) -> int:
    if n < 0:
        return 0
    if n == 1:
        return 1
    return 2 * count_points(n - 1)


res = 0
for line in _input.split("\n"):
    _, nums = line.split(":")
    winning, ours = map(parse_int_line, nums.split("|"))
    common_nums = len(winning.intersection(ours))
    res += count_points(common_nums)

print(res)
