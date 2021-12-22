cubes = []

#cube2 in cube1
def entirelyin(cube1, cube2):
    return cube2[1] >= cube1[1] and cube2[2] <= cube1[2] and cube2[3] >= cube1[3] and cube2[4] <= cube1[4] and cube2[5] >= cube1[5] and cube2[6] <= cube1[6]

def intersect(cube1, cube2):
    for x in [cube2[1], cube2[2]]:
        for y in [cube2[3], cube2[4]]:
            for z in [cube2[5], cube2[6]]:
                if cube2[1] > cube1[1] and cube2[1] <= cube1[2] and y >= cube1[3] and y <= cube1[4] and z >= cube1[5] and z <= cube1[6]:
                    return (0, cube2[1] - 1)
                if cube2[2] >= cube1[1] and cube2[2] < cube1[2] and y >= cube1[3] and y <= cube1[4] and z >= cube1[5] and z <= cube1[6]:
                    return (0, cube2[2])
                if x >= cube1[1] and x <= cube1[2] and cube2[3] > cube1[3] and cube2[3] <= cube1[4] and z >= cube1[5] and z <= cube1[6]:
                    return (1, cube2[3] - 1)
                if x >= cube1[1] and x <= cube1[2] and cube2[4] >= cube1[3] and cube2[4] < cube1[4] and z >= cube1[5] and z <= cube1[6]:
                    return (1, cube2[4])
                if x >= cube1[1] and x <= cube1[2] and y >= cube1[3] and y <= cube1[4] and cube2[5] > cube1[5] and cube2[5] <= cube1[6]:
                    return (2, cube2[5] - 1)
                if x >= cube1[1] and x <= cube1[2] and y >= cube1[3] and y <= cube1[4] and cube2[6] >= cube1[5] and cube2[6] < cube1[6]:
                    return (2, cube2[6])
    for x in [cube1[1], cube1[2]]:
        for y in [cube1[3], cube1[4]]:
            for z in [cube1[5], cube1[6]]:
                if cube1[1] < cube2[1] and cube1[2] >= cube2[1] and y >= cube2[3] and y <= cube2[4] and z >= cube2[5] and z <= cube2[6]:
                    return (0, cube2[1] - 1)
                if cube1[1] <= cube2[2] and cube1[2] > cube2[2] and y >= cube2[3] and y <= cube2[4] and z >= cube2[5] and z <= cube2[6]:
                    return (0, cube2[2])
                if x >= cube2[1] and x <= cube2[2] and cube1[3] < cube2[3] and cube1[4] >= cube2[3] and z >= cube2[5] and z <= cube2[6]:
                    return (1, cube2[3] - 1)
                if x >= cube2[1] and x <= cube2[2] and cube1[3] <= cube2[4] and cube1[4] > cube2[4] and z >= cube2[5] and z <= cube2[6]:
                    return (1, cube2[4])
                if x >= cube2[1] and x <= cube2[2] and y >= cube2[3] and y <= cube2[4] and cube1[5] < cube2[5] and cube1[6] >= cube2[5]:
                    return (2, cube2[5] - 1)
                if x >= cube2[1] and x <= cube2[2] and y >= cube2[3] and y <= cube2[4] and cube1[5] <= cube2[6] and cube1[5] > cube2[6]:
                    return (2, cube2[6])
    return None

def splitcube(cube, spl):
    if spl[0] == 0:
        return [(cube[0], cube[1], spl[1], cube[3], cube[4], cube[5], cube[6]), (cube[0], spl[1] + 1, cube[2], cube[3], cube[4], cube[5], cube[6])]
    if spl[0] == 1:
        return [(cube[0], cube[1], cube[2], cube[3], spl[1], cube[5], cube[6]), (cube[0], cube[1], cube[2], spl[1] + 1, cube[4], cube[5], cube[6])]
    return [(cube[0], cube[1], cube[2], cube[3], cube[4], cube[5], spl[1]), (cube[0], cube[1], cube[2], cube[3], cube[4], spl[1] + 1, cube[6])]

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(",")
        on = spl[0][:2] == "on"
        lowx = int(spl[0][spl[0].index("=")+1:spl[0].index(".")])
        highx = int(spl[0][spl[0].index(".")+2:])
        lowy = int(spl[1][spl[1].index("=")+1:spl[1].index(".")])
        highy = int(spl[1][spl[1].index(".")+2:])
        lowz = int(spl[2][spl[2].index("=")+1:spl[2].index(".")])
        highz = int(spl[2][spl[2].index(".")+2:])
        cubes.append((on, lowx, highx, lowy, highy, lowz, highz))

i = 1
while i < len(cubes):
    j = 0
    while j < i:
        if entirelyin(cubes[i], cubes[j]):
            cubes.pop(j)
            i -= 1
        elif not (spl := intersect(cubes[i], cubes[j])) is None:
            splcubes = splitcube(cubes.pop(i), spl)
            cubes.insert(i, splcubes[0])
            cubes.insert(i, splcubes[1])
        elif not (spl := intersect(cubes[j], cubes[i])) is None:
            splcubes = splitcube(cubes.pop(j), spl)
            cubes.insert(j, splcubes[0])
            cubes.insert(j, splcubes[1])
            i += 1
        else:
            j += 1
    
    if cubes[i][0]:
        i += 1
    else:
        cubes.pop(i)

onsum = 0
for cube in cubes:
    onsum += (cube[2] - cube[1] + 1) * (cube[4] - cube[3] + 1) * (cube[6] - cube[5] + 1)

print(onsum)