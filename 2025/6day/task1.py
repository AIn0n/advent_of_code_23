import pandas as pd
from operator import add, mul
from functools import reduce

OP = {
    "+": add,
    "*": mul
}

INIT = {
    "+": 0,
    "*": 1,
}


def solution(input_path: str) -> int:
    df = pd.read_csv(input_path, sep=" +", header=None)
    operators = list(df.iloc[-1])
    df: pd.DataFrame = df.iloc[:-1].astype(int)
    res = 0
    for col, op in zip(df.columns, operators):
        res += reduce(lambda x, y: OP[op](x, y), df[col], INIT[op])
    return res

if __name__ == "__main__":
    print(solution("valid_input.txt"))
