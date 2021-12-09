map = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        map.append(line)
basins = []
for x in range(len(map[0])):
    for y in range(len(map)):
        if x > 0 and map[y][x-1] <= map[y][x]:
            continue
        if x < len(map[0]) - 1 and map[y][x+1] <= map[y][x]:
            continue
        if y > 0 and map[y-1][x] <= map[y][x]:
            continue
        if y < len(map) - 1 and map[y+1][x] <= map[y][x]:
            continue
        basin = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
        basin[y][x] = True
        run = True
        while run:
            run = False
            for x2 in range(len(map[0])):
                for y2 in range(len(map)):
                    if basin[y2][x2]:
                        if x2 > 0 and not basin[y2][x2-1] and map[y2][x2-1] > map[y2][x2] and map[y2][x2-1] < '9':
                            basin[y2][x2-1] = True
                            run = True
                        if x2 < len(map[0]) - 1 and not basin[y2][x2+1] and map[y2][x2+1] > map[y2][x2] and map[y2][x2+1] < '9':
                            basin[y2][x2+1] = True
                            run = True
                        if y2 > 0 and not basin[y2-1][x2] and map[y2-1][x2] > map[y2][x2] and map[y2-1][x2] < '9':
                            basin[y2-1][x2] = True
                            run = True
                        if y2 < len(map) - 1 and not basin[y2+1][x2] and map[y2+1][x2] > map[y2][x2] and map[y2+1][x2] < '9':
                            basin[y2+1][x2] = True
                            run = True
        basins.append(sum([sum(i) for i in basin]))
basins.sort()
print(basins[-1] * basins[-2] * basins[-3])