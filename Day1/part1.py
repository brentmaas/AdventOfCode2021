inc = 0
with open("Input.txt", "r") as f:
    prev = int(f.readline())
    while line:= f.readline():
        val = int(line)
        if val > prev:
            inc += 1
        prev = val
print(inc)