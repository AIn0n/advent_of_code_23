from collections import Counter

lines = None
with open("input.txt", "rt") as f:
    lines = f.readlines()

first_list = []
second_list = []
for line in lines:
    first, second = line[:-1].split()
    first_list.append(int(first))
    second_list.append(int(second))

counter = Counter(second_list)

mul_list = map(lambda x: x * counter[x], first_list)

print(sum(mul_list))