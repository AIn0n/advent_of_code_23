from copy import deepcopy

from task1 import is_paper, is_valid

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

def solution(old: list[str]) -> int:
    old = [[col for col in row] for row in old]
    res = 0
    diff = 0
    new = deepcopy(old)
    while True:
        for y in range(len(old)):
            for x in range(len(old[y])):
                if not is_paper(old, y, x):
                    continue
                counter = map(
                    lambda n: is_valid(old, y + n[0], x + n[1]) and is_paper(old, y + n[0], x + n[1]),
                    POS
                )
                if sum(counter) < 4:
                    res += 1
                    diff += 1
                    new[y][x] = "."
        if diff == 0:
            break
        diff = 0
        old = new
        new = deepcopy(old)
    return res


if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))