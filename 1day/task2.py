from string import digits
import re

str_int = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

convert = {}
rev_convert = {}

for idx, s in enumerate(str_int):
    convert[s] = idx + 1
    rev_convert[s[::-1]] = idx + 1

for idx, s in enumerate(digits[1:]):
    convert[s] = idx + 1
    rev_convert[s] = idx + 1

regex = "(" + "|".join(convert.keys()) + ")"
rev_regex = "(" + "|".join(rev_convert.keys()) + ")"

suma = 0
with open("in.txt", "rt") as f:
    for line in f.read().split():
        first = re.search(regex, line).group()
        second = re.search(rev_regex, line[::-1]).group()
        suma += convert[first] * 10 + rev_convert[second]

print(suma)
