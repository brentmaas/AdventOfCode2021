states = [([[], [], [], []], ["." for _ in range(11)], 0)]
with open("Input.txt", "r") as f:
    f.readline()
    f.readline()
    for _ in range(2):
        spl = f.readline()[3:10].split("#")
        for i in range(4):
            states[0][0][i].append(spl[i])

energy = {"A": 1, "B": 10, "C": 100, "D": 1000}
dest = {"A": 0, "B": 1, "C": 2, "D": 3}

def check(rooms):
    return rooms[0][0] == "A" and rooms[0][1] == "A" and rooms[1][0] == "B" and rooms[1][1] == "B" and rooms[2][0] == "C" and rooms[2][1] == "C" and rooms[3][0] == "D" and rooms[3][1] == "D"

def hallempty(hall, low=0, high=11):
    return all([c == "." for c in hall[min(low, high)+1:max(low, high)]])

minenergy = 2e9

while len(states) > 0:
    rooms = [[states[0][0][0][0], states[0][0][0][1]], [states[0][0][1][0], states[0][0][1][1]], [states[0][0][2][0], states[0][0][2][1]], [states[0][0][3][0], states[0][0][3][1]]]
    hall = [c for c in states[0][1]]
    e = states[0][2]
    
    run = True
    while run:
        run = False
        for j in [0, 1, 3, 5, 7, 9, 10]:
            if hall[j] != "." and rooms[(d := dest[hall[j]])][0] == "." and hallempty(hall, 2 * d + 2, j):
                if rooms[d][1] == hall[j]:
                    rooms[d][0], hall[j] = hall[j], rooms[d][0]
                    e += (abs(2 * d + 2 - j) + 1) * energy[rooms[d][0]]
                    run = True
                elif rooms[d][1] == ".":
                    rooms[d][1], hall[j] = hall[j], rooms[d][1]
                    e += (abs(2 * d + 2 - j) + 2) * energy[rooms[d][1]]
                    run = True
    
    didsomething = False
    if e < minenergy:
        for i in range(4):
            for j in [0, 1, 3, 5, 7, 9, 10]:
                if hall[j] == "." and hallempty(hall, 2 * i + 2, j):
                    if rooms[i][0] != "." and (dest[rooms[i][0]] != i or dest[rooms[i][1]] != i):
                        newrooms = [[rooms[0][0], rooms[0][1]], [rooms[1][0], rooms[1][1]], [rooms[2][0], rooms[2][1]], [rooms[3][0], rooms[3][1]]]
                        newhall = [c for c in hall]
                        newrooms[i][0], newhall[j] = newhall[j], newrooms[i][0]
                        states.insert(1, (newrooms, newhall, e + (abs(2 * i + 2 - j) + 1) * energy[newhall[j]]))
                        didsomething = True
                    elif rooms[i][0] == "." and rooms[i][1] != "." and dest[rooms[i][1]] != i:
                        newrooms = [[rooms[0][0], rooms[0][1]], [rooms[1][0], rooms[1][1]], [rooms[2][0], rooms[2][1]], [rooms[3][0], rooms[3][1]]]
                        newhall = [c for c in hall]
                        newrooms[i][1], newhall[j] = newhall[j], newrooms[i][1]
                        states.insert(1, (newrooms, newhall, e + (abs(2 * i + 2 - j) + 2) * energy[newhall[j]]))
                        didsomething = True
    
    if not didsomething and e < minenergy and check(rooms):
        minenergy = e
    states.pop(0)

print(minenergy)