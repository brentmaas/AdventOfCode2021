#This function is done by hand from the input
def run(inp):
    inp = str(inp)
    
    a = 0 if int(inp[2]) - 3 == int(inp[3]) else 1
    b = 0 if int(inp[5]) + 3 == int(inp[6]) else 1
    c = 0 if ((int(inp[6]) - 3) if b == 1 else (int(inp[4]) + 2)) == int(inp[7]) else 1
    d = 0 if int(inp[8]) - 5 == int(inp[9]) else 1
    e = 0 if int(inp[10]) - 1 == int(inp[11]) else 1
    
    if e == 1:
        f = 0 if int(inp[11]) + 7 == int(inp[12]) else 1
    elif d == 1:
        f = 0 if int(inp[9]) + 4 == int(inp[12]) else 1
    elif c == 1 or b == 1:
        f = 1
    elif a == 1:
        f = 0 if int(inp[3]) + 6 == int(inp[12]) else 1
    else:
        f = 0 if int(inp[1]) + 7 == int(inp[12]) else 1
    
    if f == 1:
        g = 0 if int(inp[12]) + 1 == int(inp[13]) else 1
    elif e == 1 and d == 1:
        g = 0 if int(inp[9]) - 7 == int(inp[13]) else 1
    elif e == 1 and c == 1:
        g = 0 if int(inp[7]) - 2 == int(inp[13]) else 1
    elif e == 1 and b == 1:
        g = 0 if int(inp[4]) + 3 == int(inp[13]) else 1
    elif e == 1 and a == 1:
        g = 0 if int(inp[3]) - 5 == int(inp[13]) else 1
    elif e == 1:
        g = 0 if int(inp[1]) - 4 == int(inp[13]) else 1
    elif d == 1 and c == 1:
        g = 0 if int(inp[7]) - 2 == int(inp[13]) else 1
    elif d == 1 and b == 1:
        g = 0 if int(inp[4]) + 3 == int(inp[13]) else 1
    elif d == 1 and a == 1:
        g = 0 if int(inp[3]) - 5 == int(inp[13]) else 1
    elif d == 1:
        g = 0 if int(inp[1]) - 4 == int(inp[13]) else 1
    elif c == 1 and b == 1:
        g = 0 if int(inp[4]) + 3 == int(inp[13]) else 1
    elif c == 1 and a == 1:
        g = 0 if int(inp[3]) - 5 == int(inp[13]) else 1
    elif c == 1:
        g = 0 if int(inp[1]) - 4 == int(inp[13]) else 1
    elif b == 1 and a == 1:
        g = 0 if int(inp[3]) - 5 == int(inp[13]) else 1
    elif b == 1:
        g = 0 if int(inp[1]) - 4 == int(inp[13]) else 1
    elif a == 1:
        g = 0 if int(inp[1]) - 4 == int(inp[13]) else 1
    else:
        g = 0 if int(inp[0]) - 8 == int(inp[13]) else 1
    
    z = 26 * (int(inp[0]) + 3) + int(inp[1]) + 7
    z *= 25 * a + 1
    z += (int(inp[3]) + 6) * a
    z *= 26
    z += int(inp[4]) + 14
    z *= 25 * b + 1
    z += (int(inp[6]) + 9) * b
    z = int(z / 26)
    z *= 25 * c + 1
    z += (int(inp[7]) + 9) * c
    z *= 25 * d + 1
    z += (int(inp[9]) + 4) * d
    z *= 25 * e + 1
    z += (int(inp[11]) + 7) * e
    z = int(z / 26)
    z *= 25 * f + 1
    z += (int(inp[12]) + 12) * f
    z = int(z / 26)
    z *= 25 * g + 1
    z += (int(inp[13]) + 1) * g
    
    return z == 0

def solve(a, b, c, d, e, f, g):
    inp = [1 for _ in range(14)]
    
    if a == 0:
        inp[2] = inp[3] + 3
    if b == 0:
        inp[6] = inp[5] + 3
    if c == 0:
        if b == 1:
            inp[6] = inp[7] + 3
        else:
            inp[7] = inp[4] + 2
    if d == 0:
        inp[8] = inp[9] + 5
    if e == 0:
        inp[10] = inp[11] + 1
    
    if f == 0:
        if e == 1:
            inp[12] = inp[11] + 7
        elif d == 1:
            inp[12] = inp[9] + 4
        elif c == 1 or b == 1:
            return "0" * 14
        elif a == 1:
            inp[12] = inp[3] + 6
        else:
            inp[12] = inp[1] + 7
    
    if g == 0:
        if f == 1:
            inp[13] = inp[12] + 1
        elif e == 1 and d == 1:
            inp[9] = inp[13] + 7
        elif e == 1 and c == 1:
            inp[7] = inp[13] + 2
        elif e == 1 and b == 1:
            inp[13] = inp[4] + 3
        elif e == 1 and a == 1:
            inp[3] = inp[13] + 5
        elif e == 1:
            inp[1] = inp[13] + 4
        elif d == 1 and c == 1:
            inp[7] = inp[13] + 2
        elif d == 1 and b == 1:
            inp[13] = inp[4] + 3
        elif d == 1 and a == 1:
            inp[3] = inp[13] + 5
        elif d == 1:
            inp[1] = inp[13] + 4
        elif c == 1 and b == 1:
            inp[13] = inp[4] + 3
        elif c == 1 and a == 1:
            inp[3] = inp[13] + 5
        elif c == 1:
            inp[1] = inp[13] + 4
        elif b == 1 and a == 1:
            inp[3] = inp[13] + 5
        elif b == 1 or a == 1:
            inp[1] = inp[13] + 4
        else:
            inp[0] = inp[13] + 8
    
    if not all([i >= 1 and i <= 9 for i in inp]):
        return "0" * 14
    
    return str("".join([str(i) for i in inp]))

minval = 1e15
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            for d in [0, 1]:
                for e in [0, 1]:
                    for f in [0, 1]:
                        for g in [0, 1]:
                            val = solve(a, b, c, d, e, f, g)
                            if run(val) and int(val) < minval:
                                minval = val
print(minval)