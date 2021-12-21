with open("Input.txt", "r") as f:
    p1 = int(f.readline().rstrip()[-1])
    p2 = int(f.readline().rstrip()[-1])
pos = [p1, p2]
score = [0, 0]
die = 1
turn = 0
rolls = 0

while score[0] < 1000 and score[1] < 1000:
    roll = 3 * die + 3
    die = (die + 2) % 100 + 1
    rolls += 3
    pos[turn] = (pos[turn] + roll - 1) % 10 + 1
    score[turn] += pos[turn]
    turn = 1 - turn

print(score[turn] * rolls)