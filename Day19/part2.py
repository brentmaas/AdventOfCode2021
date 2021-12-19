data = []
with open("Input.txt", "r") as f:
    while "scanner" in (line := f.readline().rstrip()):
        scanner = []
        while line := f.readline().rstrip():
            scanner.append([int(i) for i in line.split(",")])
        data.append(scanner)

rot = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

def findoverlap(s1, s2):
    for rx in range(6):
        for ry in range(6):
            for rz in range(6):
                if (rx % 3) != (ry % 3) and (rx % 3) != (rz % 3) and (ry % 3) != (rz % 3):
                    rotx = rot[rx]
                    roty = rot[ry]
                    rotz = rot[rz]
                    for i in range(len(s1)):
                        for j in range(len(s2)):
                            dx = s1[i][0] - (rotx[0] * s2[j][0] + roty[0] * s2[j][1] + rotz[0] * s2[j][2])
                            dy = s1[i][1] - (rotx[1] * s2[j][0] + roty[1] * s2[j][1] + rotz[1] * s2[j][2])
                            dz = s1[i][2] - (rotx[2] * s2[j][0] + roty[2] * s2[j][1] + rotz[2] * s2[j][2])
                            count = 0
                            for k in range(len(s2)):
                                if [rotx[0] * s2[k][0] + roty[0] * s2[k][1] + rotz[0] * s2[k][2] + dx, rotx[1] * s2[k][0] + roty[1] * s2[k][1] + rotz[1] * s2[k][2] + dy, rotx[2] * s2[k][0] + roty[2] * s2[k][1] + rotz[2] * s2[k][2] + dz] in s1:
                                    count += 1
                            if count >= 12:
                                return [dx, dy, dz], [rotx, roty, rotz]
    
    return None, None

found = [False for _ in range(len(data))]
found[0] = True
tried = [[] for _ in range(len(data))]
pos = [None for _ in range(len(data))]
pos[0] = [0, 0, 0]
while sum(found) < len(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if found[i] and not found[j] and not i in tried[j]:
                tried[j].append(i)
                t, r = findoverlap(data[i], data[j])
                pos[j] = t
                if not t is None:
                    found[j] = True
                    for k in range(len(data[j])):
                        x = r[0][0] * data[j][k][0] + r[1][0] * data[j][k][1] + r[2][0] * data[j][k][2] + t[0]
                        y = r[0][1] * data[j][k][0] + r[1][1] * data[j][k][1] + r[2][1] * data[j][k][2] + t[1]
                        z = r[0][2] * data[j][k][0] + r[1][2] * data[j][k][1] + r[2][2] * data[j][k][2] + t[2]
                        data[j][k][0] = x
                        data[j][k][1] = y
                        data[j][k][2] = z

maxdist = 0
for i in range(len(data)):
    for j in range(len(data)):
        dist = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]) + abs(pos[i][2] - pos[j][2])
        if dist > maxdist:
            maxdist = dist
print(maxdist)