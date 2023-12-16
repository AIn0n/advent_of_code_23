import networkx as nx
import matplotlib.pyplot as plt

_input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF""".split("\n")

char_to_dirs = {
    "-" : [False, True, False, True],
    "|" : [True, False, True, False],
    "L" : [True, True, False, False],
    "F" : [False, True, True, False],
    "J" : [True, False, False, True],
    "7" : [False, False, True, True],
    "." : [False, False, False, False],
    "S" : [True, True, True, True]
}

legal_dirs = {
    "-" : [[(-1, 0), (1, 0)], [3, 1]],
    "|" : [[(0, -1), (0, 1)], [2, 0]],
    "L" : [[(-1, 0), (1, 0)], [2, 3]],
    "F" : [[(1, 0), (0, 1)],  [0, 3]],
    "7" : [[(1, 0), (0, -1)], [0, 1]],
    "J" : [[(-1, 0), (0, -1)],[3, 1]],
    ".": [[], []],
    "S": [[(1, 0), (-1, 0), (0, 1), (0, -1)], [0, 2, 3, 1]]
}

graph = {}


for y in range(len(_input)):
    for x in range(len(_input[0])):
        print("working with", x, y)
        connections = []
        for pos, check in zip(*legal_dirs[_input[y][x]]):
            print(pos, check)
            curr_x, curr_y = pos
            curr_x += x
            curr_y += y
            if curr_x < 0 or curr_y < 0 or curr_x >= len(_input[0]) or curr_y >= len(_input):
                break
            if char_to_dirs[_input[curr_y][curr_x]][check] == True:
                print(True)
                connections.append(tuple([curr_y, curr_x]))
        graph[tuple([y, x])] = connections



G = nx.Graph(graph)
DG = nx.DiGraph(G)

nx.draw(DG, with_labels=True, font_weight='bold')

plt.show()

for p in list(nx.simple_cycles(DG)):
    print(p)