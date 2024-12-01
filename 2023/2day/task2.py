from collections import defaultdict

with open("in.txt", "rt") as f:
    res = 0
    for line in f.read().split("\n"):
        prefix, games = line.split(":")
        id = int(prefix.split(" ")[-1])
        minimas = defaultdict(int)
        for game in games.split(";"):
            for color in game.split(","):
                _, num, col = color.split(" ")
                minimas[col] = max(minimas[col], int(num))
        res += minimas["green"] * minimas["red"] * minimas["blue"]
    print(res)
