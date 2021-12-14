xs = []
ys = []
with open("Input.txt", "r") as f:
    while line := f.readline():
        if line == "\n":
            break
        x, y = line.rstrip().split(",")
        xs.append(int(x))
        ys.append(int(y))
    while line := f.readline().rstrip():
        fold = int(line[line.index("=")+1:])
        if "x" in line:
            for i in range(len(xs)):
                xs[i] = fold - abs(xs[i] - fold)
        else:
            for i in range(len(ys)):
                ys[i] = fold - abs(ys[i] - fold)
paper = [[" " for _ in range(max(xs)+1)] for _ in range(max(ys)+1)]
for i in range(len(xs)):
    paper[ys[i]][xs[i]] = "#"
for row in paper:
    print("".join(row))