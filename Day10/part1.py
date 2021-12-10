score = 0
other = {")": "(", "]": "[", "}": "{", ">": "<"}
dscore = {")": 3, "]": 57, "}": 1197, ">": 25137}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        stack = []
        for c in line:
            if c in other:
                if other[c] != stack.pop():
                    score += dscore[c]
                    break
            else:
                stack.append(c)
print(score)