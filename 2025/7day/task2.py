from collections import defaultdict
from copy import deepcopy

def solution(rows: list[str]) -> int:
    beams_pos = defaultdict(int)
    beams_pos[rows[0].find("S")] = 1

    for row in rows[1:]:
        if row.find("^") == -1:
            continue
        new_beams_pos = defaultdict(int)
        for idx in range(len(row)):
            if row[idx] != "^":
                continue
            if idx in beams_pos:
                curr_splits = beams_pos[idx]
                new_beams_pos[idx - 1] += curr_splits
                new_beams_pos[idx + 1] += curr_splits
                del beams_pos[idx]
        for k, v in new_beams_pos.items():
            beams_pos[k] += v
    
    return sum(beams_pos.values())



if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))
