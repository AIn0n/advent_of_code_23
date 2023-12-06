
class Range:
    def __init__(self, start, l) -> None:
        self.start = start
        self._len = l
        self.end = self.start + self._len - 1