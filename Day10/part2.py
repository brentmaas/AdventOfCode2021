scores = []
other = {")": "(", "]": "[", "}": "{", ">": "<"}
dscore = {"(": 1, "[": 2, "{": 3, "<": 4}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        stack = []
        corrupt = False
        for c in line:
            if c in other:
                if other[c] != stack.pop():
                    corrupt = True
                    break
            else:
                stack.append(c)
        if not corrupt:
            score = 0
            while len(stack) > 0:
                score *= 5
                score += dscore[stack.pop()]
            scores.append(score)
scores.sort()
print(scores[len(scores)//2])