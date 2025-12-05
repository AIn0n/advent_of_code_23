from itertools import chain

# if second start or end is between first one values
def is_overlapping(first: tuple[int], second: tuple[int]) -> bool:
    first_start, first_end = first[0], first[1]
    second_start, second_end = second[0], second[1]
    return (
        first_start <= second_start <= first_end or
        first_start <= second_end <= first_end
    )

def merge_ranges(first: tuple[int], second: tuple[int]) -> tuple[int]:
    first_start, first_end = first[0], first[1]
    second_start, second_end = second[0], second[1]
    return tuple([min(first_start, second_start), max(first_end, second_end)])

def solution(rows: list[str]) -> int:
    ranges = []
    for row in rows:
        if row[0] == "\n":
            break
        ranges.append(tuple(int(el) for el in row[:-1].split("-")))

    for _ in range(len(ranges)):
        r = ranges.pop(0)
        leaved = []
        for el in ranges:
            if is_overlapping(r, el):
                r = merge_ranges(r, el)
            else:
                leaved.append(el)
        leaved.append(r)
        ranges = leaved

    return sum(map(lambda n: n[1] - n[0] + 1, ranges))


if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))