with open("in.txt", "rt") as f:
    valid = 0
    for line in f.readlines():
        lvls = [int(x) for x in line.split()]
        sorted_lvls = sorted(lvls)
        if not (lvls == sorted_lvls or lvls == [*reversed(sorted_lvls)]):
            continue

        diff = map(lambda x: 1 <= abs(x[0] - x[1]) <= 3, zip(lvls[1:], lvls[:-1]))

        if all(diff):
            valid += 1

    print(valid)
