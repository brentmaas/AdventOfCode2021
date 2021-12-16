cave = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        cave.append([int(c) for c in line])
risk = [[2e9 for _ in range(len(cave[0]))] for _ in range(len(cave))]
risk[0][0] = 0
run = True
while run:
    run = False
    for x in range(len(cave[0])):
        for y in range(len(cave)):
            if x > 0 and risk[y][x-1] + cave[y][x] < risk[y][x]:
                risk[y][x] = risk[y][x-1] + cave[y][x]
                run = True
            if x < len(cave[0]) - 1 and risk[y][x+1] + cave[y][x] < risk[y][x]:
                risk[y][x] = risk[y][x+1] + cave[y][x]
                run = True
            if y > 0 and risk[y-1][x] + cave[y][x] < risk[y][x]:
                risk[y][x] = risk[y-1][x] + cave[y][x]
                run = True
            if y < len(cave) - 1 and risk[y+1][x] + cave[y][x] < risk[y][x]:
                risk[y][x] = risk[y+1][x] + cave[y][x]
                run = True
print(risk[-1][-1])