map = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        map.append(line)
risk = 0
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
        risk += int(map[y][x]) + 1
print(risk)