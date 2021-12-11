energies = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        energies.append([int(c) for c in line])

flashes = 0
for _ in range(100):
    for x in range(len(energies[0])):
        for y in range(len(energies)):
            energies[y][x] += 1
    checkflash = True
    hasflashed = [[False for _ in range(len(energies[0]))] for _ in range(len(energies))]
    while checkflash:
        checkflash = False
        for x in range(len(energies[0])):
            for y in range(len(energies)):
                if energies[y][x] > 9:
                    flashes += 1
                    checkflash = True
                    energies[y][x] = 0
                    hasflashed[y][x] = True
                    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        if x + dx >= 0 and x + dx < len(energies[0]) and y + dy >= 0 and y + dy < len(energies) and not hasflashed[y+dy][x+dx]:
                            energies[y+dy][x+dx] += 1

print(flashes)