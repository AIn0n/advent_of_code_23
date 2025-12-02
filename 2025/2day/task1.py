import re

TEST_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def is_repetition(num: int) -> bool:
    seq = ""
    str_num = str(num)
    len_num = len(str_num)
    if len_num % 2 != 0:
        return False
    for digit in str_num[:(len_num // 2)]:
        seq += digit
        find_res = re.findall(seq, str_num)
        if "".join(find_res) == str_num:
            return True
    return False


def solution(inp: str) -> int:
    splitted = inp.split(",")
    res = []
    for el in splitted:
        start, end = el.split("-")
        start, end = int(start), int(end)
        invalid_ids = [el for el in range(start, end + 1) if is_repetition(el)]
        print(f"({start} - {end}) = {invalid_ids}")
        res.extend(invalid_ids)
    return sum(res)



if __name__ == "__main__":
    print(solution(TEST_INPUT))