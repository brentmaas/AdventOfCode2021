n = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line[line.index("|")+1:].split(" ")
        for s in spl:
            if len(s) in [2, 3, 4, 7]:
                n += 1
print(n)