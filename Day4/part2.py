boards = []
with open("Input.txt", "r") as f:
    nums = [int(i) for i in f.readline().rstrip().split(",")]
    while f.readline():
        board = []
        for _ in range(5):
            board.append([int(i) for i in f.readline().rstrip().split()])
        boards.append(board)
marked = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]

def mark(i):
    for j in range(len(boards)):
        for k in range(5):
            if i in boards[j][k]:
                marked[j][k][boards[j][k].index(i)] = True

def check(i):
    for j in range(5):
        if sum(marked[i][j]) == 5 or (marked[i][0][j] and marked[i][1][j] and marked[i][2][j] and marked[i][3][j] and marked[i][4][j]):
            return True
    return False

def score(i):
    s = 0
    for j in range(5):
        for k in range(5):
            if not marked[i][j][k]:
                s += boards[i][j][k]
    return s

for i in range(4):
    mark(nums[i])

won = [False] * len(boards)

for i in range(4, len(nums)):
    mark(nums[i])
    for j in range(len(boards)):
        if check(j):
            won[j] = True
            if sum(won) == len(boards):
                print(score(j) * nums[i])
                exit()