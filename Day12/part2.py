cavemap = {}
twice = {}
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
        twice[left] = left >= "a"
        twice[right] = right >= "a"

def checktwicegood(path):
    twiceloc = None
    for loc in path:
        if twice[loc] and sum([loc == l for l in path]) > 1:
            if twiceloc is None:
                twiceloc = loc
                break
    return not (not twiceloc is None and cavemap[path[-1]][indices[-1]] in path)

paths = []
path = ["start"]
indices = [0]
while len(path) > 0:
    if len(cavemap[path[-1]]) > indices[-1]:
        if cavemap[path[-1]][indices[-1]] == "end":
            paths.append(",".join(path) + ",end")
            indices[-1] += 1
        elif cavemap[path[-1]][indices[-1]] == "start" or (twice[cavemap[path[-1]][indices[-1]]] and not checktwicegood(path)):
            indices[-1] += 1
        else:
            path.append(cavemap[path[-1]][indices[-1]])
            indices[-1] += 1
            indices.append(0)
    else:
        path.pop()
        indices.pop()
print(len(paths))