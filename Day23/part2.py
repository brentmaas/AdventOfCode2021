states = [([["D", "D"], ["C", "B"], ["B", "A"], ["A", "C"]], ["." for _ in range(11)], 0)]
with open("Input.txt", "r") as f:
    f.readline()
    f.readline()
    spl = f.readline()[3:10].split("#")
    for i in range(4):
        states[0][0][i].insert(0, spl[i])
    spl = f.readline()[3:10].split("#")
    for i in range(4):
        states[0][0][i].append(spl[i])

energy = {"A": 1, "B": 10, "C": 100, "D": 1000}
dest = {"A": 0, "B": 1, "C": 2, "D": 3}

def check(rooms):
    return all([c == "A" for c in rooms[0]]) and all([c == "B" for c in rooms[1]]) and all([c == "C" for c in rooms[2]]) and all([c == "D" for c in rooms[3]])

def hallempty(hall, low=0, high=11):
    return all([c == "." for c in hall[min(low, high)+1:max(low, high)]])

minenergy = 2e9

while len(states) > 0:
    rooms = [[c for c in states[0][0][0]], [c for c in states[0][0][1]], [c for c in states[0][0][2]], [c for c in states[0][0][3]]]
    hall = [c for c in states[0][1]]
    e = states[0][2]
    top = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            if rooms[i][j] == ".":
                top[i] += 1
            else:
                break
    
    run = True
    while run:
        run = False
        for j in [0, 1, 3, 5, 7, 9, 10]:
            if hall[j] != "." and top[(d := dest[hall[j]])] > 0 and hallempty(hall, 2 * d + 2, j) and all([c == hall[j] for c in rooms[d][top[d]:]]):
                top[d] -= 1
                rooms[d][top[d]], hall[j] = hall[j], rooms[d][top[d]]
                e += (abs(2 * d + 2 - j) + top[d] + 1) * energy[rooms[d][top[d]]]
                run = True
    
    didsomething = False
    if e < minenergy:
        for i in range(4):
            for j in [0, 1, 3, 5, 7, 9, 10]:
                if hall[j] == "." and top[i] < 4 and hallempty(hall, 2 * i + 2, j) and (dest[rooms[i][top[i]]] != i or not all([c == rooms[i][top[i]] for c in rooms[i][top[i]+1:]])):
                    newrooms = [[c for c in rooms[0]], [c for c in rooms[1]], [c for c in rooms[2]], [c for c in rooms[3]]]
                    newhall = [c for c in hall]
                    newrooms[i][top[i]], newhall[j] = newhall[j], newrooms[i][top[i]]
                    states.insert(1, (newrooms, newhall, e + (abs(2 * i + 2 - j) + top[i] + 1) * energy[newhall[j]]))
                    didsomething = True
    
    if not didsomething and e < minenergy and check(rooms):
        minenergy = e
    states.pop(0)

print(minenergy)