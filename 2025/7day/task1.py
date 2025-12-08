
def solution(rows: list[str]) -> int:
    beams_pos = set([rows[0].find("S")])
    splits = 0
    for row in rows[1:]:
        new_beams_pos = set()
        for idx in range(len(row)):
            if row[idx] != "^":
                continue
            if idx in beams_pos:
                splits += 1
                new_beams_pos.add(idx - 1)
                new_beams_pos.add(idx + 1)
                beams_pos.remove(idx)
        beams_pos.update(new_beams_pos)
    
    return splits



if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))
