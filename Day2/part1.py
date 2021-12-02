pos = 0
depth = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        cmd = spl[0]
        val = int(spl[1])
        if cmd == "forward":
            pos += val
        elif cmd == "down":
            depth += val
        elif cmd == "up":
            depth -= val
print(pos * depth)