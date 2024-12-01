__input = open("in.txt", "rt").read()


def parse_int_line(s: str) -> list[int]:
    return [int(x) for x in s.split(" ") if x != ""]


def parse_map(s: str) -> list[int]:
    _, lists = s.split("map:\n")
    return [parse_int_line(l) for l in lists.split("\n")]


_maps = __input.split("\n\n")

# parse initial seeds
_, seeds = _maps[0].split(":")

res = parse_int_line(seeds)

for _map in _maps[1:]:
    for n in range(len(res)):
        for dst, src, _len in parse_map(_map):
            dist = dst - src
            if res[n] in range(src, src + _len):
                res[n] += dist
                break

print(min(res))
