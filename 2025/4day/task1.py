
def is_valid(rows: list[str], y: int, x: int) -> bool:
    max_y = len(rows) - 1
    if y < 0 or y > max_y:
        return False
    max_x = len(rows[0]) - 1
    if x < 0 or x > max_x:
        return False
    return True

def is_paper(rows: list[str], y: int, x: int) -> bool:
    return rows[y][x] == "@"

POS = (
    (-1, 0),    # N
    (1, 0),     # S
    (0, -1),    # W
    (0, 1),     # E
    (-1, -1),   # NW
    (-1, 1),    # NE
    (1, -1),    # SW
    (1, 1),     # SE
)

def solution(rows: list[str]) -> int:
    res = 0
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if not is_paper(rows, y, x):
                continue
            counter = map(
                lambda n: is_valid(rows, y + n[0], x + n[1]) and is_paper(rows, y + n[0], x + n[1]),
                POS
            )
            if sum(counter) < 4:
                res += 1
    return res


if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))