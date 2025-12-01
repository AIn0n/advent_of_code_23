from itertools import accumulate

def dec(state: int, num: int) -> int:
    res = state - num
    if res < 0:
        return (100 - abs(res)) % 100
    return res

def inc(state: int, num: int) -> int:
    res = state + num
    return res % 100

def solution(lines: list[str]) -> int:
    states = accumulate(
        lines, 
        lambda acc, el: dec(acc, int(el[1:])) if el[0] == "L" else inc(acc, int(el[1:])), 
        initial=50
    )
    states = list(states)
    print(states)
    return sum(1 for el in states if el == 0) 

if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))