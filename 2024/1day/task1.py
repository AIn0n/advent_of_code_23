from functools import reduce

lines = None
with open("input.txt", "rt") as f:
    lines = f.readlines()


first_list = []
second_list = []
for line in lines:
    first, second = line[:-1].split()
    first_list.append(int(first))
    second_list.append(int(second))

first_list.sort()
second_list.sort()

diff = reduce(lambda acc, new: acc + abs(new[0] - new[1]), zip(first_list, second_list), 0)

print(diff)