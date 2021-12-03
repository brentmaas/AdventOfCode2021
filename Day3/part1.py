n = 0
occ = [0] * 12
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        for i in range(12):
            occ[i] += int(line[i])
        n += 1
gamma = 0
epsilon = 0
for i in range(12):
    if 2 * occ[i] >= n:
        gamma += 2 ** (11 - i)
    else:
        epsilon += 2 ** (11 - i)
print(gamma * epsilon)