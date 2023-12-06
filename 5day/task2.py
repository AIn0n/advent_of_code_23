__input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""



"""
    s1               e1
    |----------------|
<-- |----------------| -->
    s2               e2

s1               e1
|----------------|
    |--------|
    s2       e2


s1    e1
|-----|
    |-----|
    s2    e2

s1  e1  s2  e2
|---|   |---|

    s1          e1
s2  |-----------|
|---------|e2


s2        e2  s1    e1
|---------|   |-----|

"""

class Range:
    def __init__(self, start: int, _len: int) -> None:
        self.s1 = start
        self._len = _len
        self.e1 = start + _len - 1

    @staticmethod
    def build_se(s, e, shift):
        return Range(s + shift, e - s)

    def cpy(self, shift=0, _len=None):
        if _len is None:
            return Range(self.s1 + shift, self._len)
        else:
            return Range(self.s1 + shift, _len)

    def __repr__(self) -> str:
        return f"range <start = {self.s1}, end = {self.e1}, len = {self._len}>"
    
    def splitable(t, s2: int, dst: int, _len: int) -> bool:
        e2 = s2 + _len
        if e2 < t.s1 or t.e1 < s2:
            return False
        return True

    def split(self, s2: int, dst: int, _len: int):
        e2 = s2 + _len

        if s2 <= self.s1 and e2 >= self.e1:
            return [self.cpy(dst - s2)]

        if s2 > self.s1 and e2 < self.e1:
            
            return [
                self.cpy(shift=0, _len= s2 - self.s1),
                Range.build_se(s2, e2, dst - s2),
                Range.build_se(e2, self.e1 + 1, 0)
            ]
        
        if self.s1 < s2:
            return [
                self.cpy(shift=0, _len = s2 - self.s1),
                Range.build_se(s2, self.e1 + 1, dst - s2)
            ]

        return [
            self.cpy(shift=dst-s2, _len=e2 - self.s1),
            Range.build_se(e2, self.e1 + 1, 0)
        ]

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

for _map in _maps[1:6]:
    _new = []
    for r in ranges:
        splitted = False
        for s in parse_map(_map):
            if r.splitable(*s):
                splitted = True
                _new += r.split(*s)
        
        if not splitted:
            _new.append(r)
    ranges = _new

for r in ranges:
    print(r)


"""for _map in _maps[1:]:
    _new = []
    for r in ranges:
        for s in parse_map(_map):
            _new += r.split(*s)
    ranges = _new.copy()
"""