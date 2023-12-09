from ranges import Range

__input = open("in.txt", "rt").read()


def parse_int_line(s: str) -> list[int]:
    return [int(x) for x in s.split(" ") if x != ""]


def parse_map(s: str) -> list[int]:
    _, lists = s.split("map:\n")
    return [parse_int_line(l) for l in lists.split("\n")]


_maps = __input.split("\n\n")

# parse initial seeds
ini = parse_int_line(_maps[0].split(":")[1])

ranges: list[Range] = []

for r in zip(ini[:-1:2], ini[1::2]):
    ranges.append(Range(*r))

for _map in _maps[1:]:
    _new = []
    for r in ranges:
        _new += r.split_by_many(_map)

    ranges = _new

print(min(ranges, key=lambda x: x.start))
