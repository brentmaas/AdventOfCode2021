vents = [[0 for _ in range(1000)] for _ in range(1000)]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl1 = line.split(" -> ")
        x1 = int(spl1[0].split(",")[0])
        y1 = int(spl1[0].split(",")[1])
        x2 = int(spl1[1].split(",")[0])
        y2 = int(spl1[1].split(",")[1])
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    vents[y][x] += 1
        else:
            n = abs(x2 - x1)
            dx = (x2 - x1) // n
            dy = (y2 - y1) // n
            for i in range(n + 1):
                vents[y1 + dy * i][x1 + dx * i] += 1
print(sum([sum([j > 1 for j in i]) for i in vents]))