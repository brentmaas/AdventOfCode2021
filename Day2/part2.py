pos = 0
depth = 0
aim = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        cmd = spl[0]
        val = int(spl[1])
        if cmd == "forward":
            pos += val
            depth += aim * val
        elif cmd == "down":
            aim += val
        elif cmd == "up":
            aim -= val
print(pos * depth)