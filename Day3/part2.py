lines = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        lines.append(line)

def rating(commonbit, uncommonbit):
    mask = [True] * len(lines)
    for i in range(12):
        occ = 0
        for j in range(len(lines)):
            occ += int(lines[j][i]) * mask[j]
        if 2 * occ >= sum(mask):
            bit = commonbit
        else:
            bit = uncommonbit
        if sum(mask) > 1:
            for j in range(len(lines)):
                if not lines[j][i] == bit:
                    mask[j] = False
    return int(lines[mask.index(True)], 2)

oxy = rating('1', '0')
co2 = rating('0', '1')
print(oxy * co2)