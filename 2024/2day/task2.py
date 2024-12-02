def elementwise_difference(l):
    return map(lambda x: 1 <= abs(x[0] - x[1]) <= 3, zip(l[1:], l[:-1]))


def in_any_order(l):
    sl = sorted(l)
    return l == sl or l == [*reversed(sl)]


with open("in.txt", "rt") as f:
    valid = 0
    for line in f.readlines():
        lvls = [int(x) for x in line.split()]
        if in_any_order(lvls):
            diff = elementwise_difference(lvls)

            if all(diff):
                valid += 1
                continue

        for i in range(len(lvls)):
            new_lvls = lvls[:i] + lvls[i + 1 :]
            if not in_any_order(new_lvls):
                continue

            diff = elementwise_difference(new_lvls)

            if all(diff):
                valid += 1
                break

    print(valid)
