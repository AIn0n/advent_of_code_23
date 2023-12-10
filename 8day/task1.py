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

curr = next(filter(lambda x: x.curr == "AAA", nodes))

i = 0
while curr.curr != "ZZZ":
    for dir in _input[0]:
        side = curr.l if dir == "L" else curr.r
        curr = next(filter(lambda x: x.curr == side, nodes))
        i += 1

print(i)
