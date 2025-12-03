import numpy as np


def solution(banks: list[str]) -> int:
    res = 0
    for bank in banks:
        nums = np.array([int(el) for el in bank[:-1]])
        max_idx = np.argmax(nums[:-1])
        res += nums[max_idx] * 10
        res += np.max(nums[max_idx + 1:])
    return res

if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))