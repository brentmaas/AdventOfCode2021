bits = ""
with open("Input.txt", "r") as f:
    line = f.readline().rstrip()
    for c in line:
        bits += f"{int(c, 16):04b}"
ptr = 0
versionsum = 0

def read(length):
    global ptr
    ret = bits[ptr:ptr+length]
    ptr += length
    return ret

def readpacket():
    global ptr, versionsum
    version = int(read(3), 2)
    versionsum += version
    id = int(read(3), 2)
    if id == 4:
        val = ""
        while True:
            group = read(5)
            val += group[1:]
            if group[0] == '0':
                break
    else:
        ltype = read(1)
        if ltype == '1':
            n = int(read(11), 2)
            for _ in range(n):
                readpacket()
        else:
            n = int(read(15), 2)
            startptr = ptr
            while ptr - startptr < n:
                readpacket()

readpacket()

print(versionsum)