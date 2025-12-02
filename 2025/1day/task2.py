from itertools import accumulate

def dec(state: tuple[int, int], num: int) -> tuple[int, int]:
    curr = state[0] - num
    if curr <= 0:
        clicks = abs(curr) // 100 + int(state[0] != 0)
        curr = (100 - abs(curr)) % 100
        return  (curr, state[1] + clicks)
    return (curr, state[1])

def inc(state: tuple[int, int], num: int) -> tuple[int, int]:
    curr = (state[0] + num) % 100
    clicks = (state[0] + num) // 100
    return (curr, state[1] + clicks)

def solution2(lines: list[str]) -> int:
    state = (50, 0)
    for el in lines:
        num = int(el[1:])
        state = dec(state, num) if el[0] == "L" else inc(state, num)
    return state[1]

if __name__ == "__main__":
    print(solution2(open("valid_input.txt").readlines()))
