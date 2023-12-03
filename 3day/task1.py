_input = open("in.txt", "rt").read()
lines = _input.replace("\n", "_\n").split("\n")

start = 0
end = 0
buffer = ""

res = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        c = lines[i][j]
        if c.isdigit():
            if len(buffer) == 0:
                start = j
            buffer += c
        elif len(buffer):
            end = j
            curr_num = int(buffer)
            neighbors = lines[i][end]
            if start > 0:
                start -= 1
                neighbors += lines[i][start]

            if i > 0:
                neighbors += lines[i - 1][start : end + 1]
            if i < len(lines) - 1:
                neighbors += lines[i + 1][start : end + 1]

            if len(neighbors.replace(".", "").replace("_", "")) != 0:
                res += curr_num
            buffer = ""

print(res)
