inc = 0
with open("Input.txt", "r") as f:
    prev1 = int(f.readline())
    prev2 = int(f.readline())
    prev3 = int(f.readline())
    while line:= f.readline():
        val = int(line)
        if prev2 + prev3 + val > prev1 + prev2 + prev3:
            inc += 1
        prev1, prev2, prev3 = prev2, prev3, val
print(inc)