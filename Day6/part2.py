fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
with open("Input.txt", "r") as f:
    for j in [int(i) for i in f.readline().rstrip().split(",")]:
        fish[j] += 1

for _ in range(256):
    newfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    newfish[6] += fish[0]
    newfish[8] += fish[0]
    for i in range(1, 9):
        newfish[i-1] += fish[i]
    fish = newfish

print(sum(fish))