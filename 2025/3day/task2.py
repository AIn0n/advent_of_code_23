import numpy as np


def solution(banks: list[str]) -> int:
    res = 0
    for bank in banks:
        nums = np.array([int(el) for el in bank[:-1]])
        jolts = 0
        for i in reversed(range(0, 12)):
            if i:
                max_idx = np.argmax(nums[:-i])
            else:
                max_idx = np.argmax(nums)
            jolts = jolts * 10 + nums[max_idx]
            nums = nums[max_idx + 1:]
        res += jolts
    return res

if __name__ == "__main__":
    print(solution(open("valid_input.txt").readlines()))