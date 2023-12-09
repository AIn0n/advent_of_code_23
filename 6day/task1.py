from math import sqrt, ceil

"""
t - total time
y - hold time
d = (t - y) * y
d = ty - y^2 

d = y^2 - ty
0 = y^2 - ty - d
a = 1
b = t
c = dist
"""


def parse_int_line(s: str) -> list[int]:
    return [int(x) for x in s.split(" ") if x != ""]


_input = """"""

time, dst = _input.split("\n")

time = parse_int_line(time.split(":")[1])
dst = parse_int_line(dst.split(":")[1])

res = 1
for t, d in zip(time, dst):
    delta = (t**2) - (4 * d)
    sqrt_delta = sqrt(delta)
    x1 = (-t + sqrt_delta) / -2
    x2 = (-t - sqrt_delta) / -2
    _min = min(x1, x2)
    _max = ceil(max(x1, x2))
    if _min == ceil(_min):
        _min = int(1 + _min)
    else:
        _min = int(ceil(_min))

    res *= len(range(_min, _max))

print(res)
