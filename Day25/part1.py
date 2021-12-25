sea = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        col = []
        for c in line:
            col.append(c)
        sea.append(col)

steps = 0
run = True
while run:
    steps += 1
    run = False
    
    for i in range(len(sea)):
        move = []
        for j in range(len(sea[0])):
            move.append(sea[i][j] == ">" and sea[i][(j+1)%len(sea[0])] == ".")
        for j in range(len(sea[0])):
            if move[j]:
                sea[i][j], sea[i][(j+1)%len(sea[0])] = sea[i][(j+1)%len(sea[0])], sea[i][j]
        if any(move):
            run = True
    
    for j in range(len(sea[0])):
        move = []
        for i in range(len(sea)):
            move.append(sea[i][j] == "v" and sea[(i+1)%len(sea)][j] == ".")
        for i in range(len(sea)):
            if move[i]:
                sea[i][j], sea[(i+1)%len(sea)][j] = sea[(i+1)%len(sea)][j], sea[i][j]
        if any(move):
            run = True

print(steps)