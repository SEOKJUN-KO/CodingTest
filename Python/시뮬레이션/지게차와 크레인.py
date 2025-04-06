from collections import deque

board = []
LY, LX = 0, 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def changeZero(y, x):
    global board, LY, LX, dx, dy
    board[y][x] = "-"
    que = deque()
    que.append([y, x])
    while(que):
        ny, nx = que.popleft()
        for i in range(4):
            Y, X = ny+dy[i], nx+dx[i]
            if 0 <= Y < LY and 0 <= X < LX and board[Y][X] == "0":
                board[Y][X] = "-"
                que.append([Y, X])

def useCar(request):
    global board, LY, LX, dx, dy
    
    arr = []
    for y in range(1, LY):
        for x in range(1, LX):
            if board[y][x] != request: continue
            for i in range(4):
                X, Y = x+dx[i], y+dy[i]
                if 0 <= Y < LY and 0 <= X < LX and board[Y][X] == "-":
                    arr.append([y, x])
    for y, x in arr:
        board[y][x] = "-"

def useCrain(request):
    global board, LY, LX, dx, dy
    for y in range(1, LY):
        for x in range(1, LX):
            if board[y][x] != request: continue
            for i in range(4):
                X, Y = x+dx[i], y+dy[i]
                board[y][x] = "0"

def solution(storage, requests):
    global board, LY, LX
    ans = 0
    out = [ "-" for _ in range(len(storage[0])+2)]
    board.append(out)
    for s in storage:
        board.append(["-"]+list(s)+["-"])
    board.append(out)
    LY = len(board)
    LX = len(board[0])
    
    for request in requests:
        if len(request) == 1:
            useCar(request)
        else:
            useCrain(request[0])
        for y in range(1, LY):
            for x in range(1, LX):
                if board[y][x] != "0": continue
                for j in range(4):
                    X, Y = x+dx[j], y+dy[j]
                    if 0 <= X < LX and 0 <= Y < LY and board[Y][X] == "-":
                        changeZero(Y, X)
    
    for y in range(1, LY):
        for x in range(1, LX):
            if (board[y][x] == "0" or board[y][x] == "-"): continue
            ans += 1
    return ans
