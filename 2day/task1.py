maxes = {"red": 12, "green": 13, "blue": 14}

with open("in.txt", "rt") as f:
    possible_ids = []
    for line in f.read().split("\n"):
        prefix, games = line.split(":")
        id = int(prefix.split(" ")[-1])
        legal = True
        for game in games.split(";"):
            curr_game = {}
            for color in game.split(","):
                _, num, col = color.split(" ")
                curr_game[col] = int(num)
            for k, v in maxes.items():
                if k in curr_game and curr_game[k] > v:
                    legal = False
                    break
        if legal:
            possible_ids.append(id)

    print(sum(possible_ids))
