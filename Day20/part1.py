with open("Input.txt", "r") as f:
    iea = [c == '#' for c in f.readline().rstrip()]
    f.readline()
    img = []
    while line := f.readline().rstrip():
        img.append([c == '#' for c in line])

fillval = False

for _ in range(2):
    newimg = []
    for i in range(-1, len(img) + 1):
        row = []
        for j in range(-1, len(img[0]) + 1):
            k = 0
            for l in range(9):
                x = j + (l % 3) - 1
                y = i + (l // 3) - 1
                if x >= 0 and x < len(img[0]) and y >= 0 and y < len(img):
                    k += 2 ** (8 - l) * img[y][x]
                else:
                    k += 2 ** (8 - l) * fillval
            row.append(iea[k])
        newimg.append(row)
    img = newimg
    fillval = iea[-1] if fillval else iea[0]

print(sum([sum(row) for row in img]))