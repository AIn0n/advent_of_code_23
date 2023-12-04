_input = open("in.txt", "rt").read()


def parse_int_line(s: str) -> set[int]:
    return set([int(x) for x in s.split(" ") if x != ""])


lines = _input.split("\n")
multiplier = [1 for _ in lines]


for i, line in enumerate(lines):
    _, nums = line.split(":")
    winning, ours = map(parse_int_line, nums.split("|"))
    common_nums = len(winning.intersection(ours))
    for n in range(common_nums):
        multiplier[i + n + 1] += 1 * multiplier[i]

print(sum(multiplier))
