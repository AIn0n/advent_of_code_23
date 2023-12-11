from math import lcm

_input = open("in.txt", "rt").read().split("\n")


class Node:
    def __init__(t, curr, l, r) -> None:
        t.curr = curr
        t.l = l
        t.r = r

    def __repr__(t) -> str:
        return f"< curr = {t.curr}, left = {t.l}, right = {t.r}>"


nodes = []


for line in _input[2:]:
    curr, next_nodes = line.split(" = ")
    left, right = next_nodes[1:-1].split(", ")
    nodes.append(Node(curr, left, right))

curr = [*filter(lambda x: x.curr[-1] == "A", nodes)]
shortest_cycle = []
for c in curr:
    i = 0
    working = True
    c1 = c
    while working:
        for dir in _input[0]:
            side = c1.l if dir == "L" else c1.r
            c1 = next(filter(lambda x: x.curr == side, nodes))
            i += 1
            if c1.curr[-1] == "Z":
                working = False
                break
    shortest_cycle.append(i)

print(lcm(*shortest_cycle))
