bits = ""
with open("Input.txt", "r") as f:
    line = f.readline().rstrip()
    for c in line:
        bits += f"{int(c, 16):04b}"
ptr = 0

def read(length):
    global ptr
    ret = bits[ptr:ptr+length]
    ptr += length
    return ret

def readpacket():
    global ptr
    version = int(read(3), 2)
    id = int(read(3), 2)
    if id == 4:
        val = ""
        while True:
            group = read(5)
            val += group[1:]
            if group[0] == '0':
                break
        val = int(val, 2)
    else:
        ltype = read(1)
        vals = []
        if ltype == '1':
            n = int(read(11), 2)
            for _ in range(n):
                vals.append(readpacket())
        else:
            n = int(read(15), 2)
            startptr = ptr
            while ptr - startptr < n:
                vals.append(readpacket())
        if id == 0:
            val = sum(vals)
        elif id == 1:
            val = 1
            for v in vals:
                val *= v
        elif id == 2:
            val = min(vals)
        elif id == 3:
            val = max(vals)
        elif id == 5:
            val = 1 if vals[0] > vals[1] else 0
        elif id == 6:
            val = 1 if vals[0] < vals[1] else 0
        elif id == 7:
            val = 1 if vals[0] == vals[1] else 0
    return val

print(readpacket())