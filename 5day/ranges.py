class Range:
    def __init__(self, start, l, shift=0) -> None:
        self.start = start
        self._len = l
        self.end = self.start + self._len - 1
        self.shift = shift

    @staticmethod
    def from_str(s: str) -> "Range":
        dst, src, l = (int(x) for x in s.split(" ") if x != "")
        return Range(src, l, shift=dst - src)

    def split(t, o: "Range") -> list["Range"]:
        return [Range(t.start + o.shift, t._len)]
