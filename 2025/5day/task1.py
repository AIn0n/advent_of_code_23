
def solution(rows: list[str]) -> int:
    ranges_flag = True
    ranges = []
    ids = []
    for row in rows:
        if row[0] == "\n":
            ranges_flag = False
            continue
        if ranges_flag:
            ranges.append(tuple(int(el) for el in row[:-1].split("-")))
        else:
            ids.append(int(row[:-1]))

    counter = 0
    for el in ids:
        for r in ranges:
            if r[0] <= el <= r[1]:
                counter += 1
                break
    return counter



if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))