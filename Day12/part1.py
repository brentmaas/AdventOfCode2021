cavemap = {}
once = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        left, right = line.split("-")
        if left in cavemap:
            cavemap[left].append(right)
        else:
            cavemap[left] = [right]
        if right in cavemap:
            cavemap[right].append(left)
        else:
            cavemap[right] = [left]
        once[left] = left >= "a"
        once[right] = right >= "a"
paths = 0
path = ["start"]
indices = [0]
while len(path) > 0:
    if len(cavemap[path[-1]]) > indices[-1]:
        if cavemap[path[-1]][indices[-1]] == "end":
            paths += 1
            indices[-1] += 1
        elif once[cavemap[path[-1]][indices[-1]]] and cavemap[path[-1]][indices[-1]] in path:
            indices[-1] += 1
        else:
            path.append(cavemap[path[-1]][indices[-1]])
            indices[-1] += 1
            indices.append(0)
    else:
        path.pop()
        indices.pop()
print(paths)