class Range:
    def __init__(self, start, l, shift=0) -> None:
        self.start = start
        self._len = l
        self.end = self.start + self._len - 1
        self.shift = shift

    def __hash__(self) -> int:
        return hash(tuple(self.start, self._len, self.end))

    @staticmethod
    def from_str(s: str) -> "Range":
        dst, src, l = (int(x) for x in s.split(" ") if x != "")
        return Range(src, l, shift=dst - src)

    def split(t, o: "Range") -> list["Range"]:
        if t.end < o.start or o.end < t.start:
            return [t]

        if t.start >= o.start and t.end <= o.end:
            return [Range(t.start + o.shift, t._len)]

        if o.start <= t.start <= o.end:
            return [
                Range(o.end + 1, t.end - o.end),
                Range(t.start + o.shift, o.end - t.start + 1),
            ]

        if o.start <= t.end <= o.end:
            return [
                Range(t.start, o.start - t.start),
                Range(o.start + o.shift, t.end - o.start + 1),
            ]

        return [
            Range(t.start, o.start - t.start),
            Range(o.start + o.shift, o._len),
            Range(o.end + 1, t.end - o.end),
        ]

    def __eq__(t, o: object) -> bool:
        if not isinstance(o, Range):
            return False

        return (t.start == o.start) and (t.end == o.end) and (t._len == o._len)

    def __repr__(t) -> str:
        return f"< start = {t.start}, end = {t.end}, len = {t._len} >"
