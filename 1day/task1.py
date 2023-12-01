from string import digits

lines = []
with open("in.txt", "rt") as f:
    lines = f.read().split()


def get_only_digits(s: str) -> str:
    return "".join(x for x in s if x in digits)


digits = [get_only_digits(x) for x in lines]
cal_vals = [int(x[0] + x[-1]) for x in digits]

print(sum(cal_vals))
