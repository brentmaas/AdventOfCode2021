with open("Input.txt", "r") as f:
    p1 = int(f.readline().rstrip()[-1])
    p2 = int(f.readline().rstrip()[-1])

states1 = [[p1, 0, 1, 0]] #pos, score, number of universes, turn
states2 = [[p2, 0, 1, 0]]

#Roll weight
rolls = {}
for r1 in range(1, 4):
    for r2 in range(1, 4):
        for r3 in range(1, 4):
            r = r1 + r2 + r3
            if r in rolls:
                rolls[r] += 1
            else:
                rolls[r] = 1

ongoingstates1 = {}
ongoingstates2 = {}
wonstates1 = {}
wonstates2 = {}

while len(states1) > 0:
    state = states1.pop(0)
    for roll in rolls:
        newpos = (state[0] + roll - 1) % 10 + 1
        newscore = state[1] + newpos
        newunis = state[2] * rolls[roll]
        newturn = state[3] + 1
        if newscore >= 21:
            if newturn in wonstates1:
                wonstates1[newturn] += newunis
            else:
                wonstates1[newturn] = newunis
        else:
            if newturn in ongoingstates1:
                ongoingstates1[newturn] += newunis
            else:
                ongoingstates1[newturn] = newunis
            states1.append([newpos, newscore, newunis, newturn])

while len(states2) > 0:
    state = states2.pop(0)
    for roll in rolls:
        newpos = (state[0] + roll - 1) % 10 + 1
        newscore = state[1] + newpos
        newunis = state[2] * rolls[roll]
        newturn = state[3] + 1
        if newscore >= 21:
            if newturn in wonstates2:
                wonstates2[newturn] += newunis
            else:
                wonstates2[newturn] = newunis
        else:
            if newturn in ongoingstates2:
                ongoingstates2[newturn] += newunis
            else:
                ongoingstates2[newturn] = newunis
            states2.append([newpos, newscore, newunis, newturn])

wins1 = 0
wins2 = 0
for i in wonstates1:
    wins1 += wonstates1[i] * ongoingstates2[i-1]
for j in wonstates2:
    if j in ongoingstates1:
        wins2 += wonstates2[j] * ongoingstates1[j]

if wins1 > wins2:
    print(wins1)
else:
    print(wins2)