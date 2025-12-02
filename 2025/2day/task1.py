import re


def is_repetition(num: int) -> bool:
    seq = ""
    str_num = str(num)
    len_num = len(str_num)
    if len_num % 2 != 0:
        return False
    for digit in str_num[:(len_num // 2)]:
        seq += digit
        find_res = re.findall(seq, str_num)
        if "".join(find_res) == str_num and len(find_res) == 2:
            return True
    return False


def solution(inp: str) -> int:
    splitted = inp.split(",")
    res = []
    for el in splitted:
        start, end = el.split("-")
        start, end = int(start), int(end)
        invalid_ids = [el for el in range(start, end + 1) if is_repetition(el)]
        res.extend(invalid_ids)
    return sum(res)



if __name__ == "__main__":
    print(solution(open("valid_input.txt").read()))