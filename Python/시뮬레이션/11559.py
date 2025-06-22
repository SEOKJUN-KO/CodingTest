import sys
from collections import deque

input = sys.stdin.readline

board = []
for _ in range(12):
    board.append(list(input().strip()))

def findFour(Y: int, X:int, target: str):
    global board
    visit = []
    visitX = set()
    que = deque()
    
    que.append([Y, X])
    visit.append([Y, X])
    visitX.add(X)

    board[Y][X] = "."
    cnt = 1
    while(que):
        popY, popX = que.popleft()
        for a, b in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            ny, nx = popY+a, popX+b
            if ( 0 <= ny < 12 and 0 <= nx < 6 and target == board[ny][nx]):
                cnt += 1
                board[ny][nx] = "."
                que.append([ny, nx])
                visit.append([ny, nx])
                visitX.add(nx)
    if cnt < 4:
        for y, x in visit:
            board[y][x] = target
        return []
    return list(visitX)

def goDown(nx):
    global board
    while(True):
        startY = -1
        targetY = -1
        for ny in range(11, -1, -1):
            if startY == -1 and board[ny][nx] == ".":
                startY = ny
            elif startY != -1 and board[ny][nx] != ".":
                targetY = ny
                break
        if (startY == -1 or targetY == -1):
            break
        for ny in range(12):
            if targetY-ny >= 0 and board[targetY-ny] != ".":
                board[startY-ny][nx] = board[targetY-ny][nx]
                board[targetY-ny][nx] = "."
            else:
                break
            

ans = 0
while(True):
    check = set()
    for y in range(11, -1, -1):
        for x in range(6):
            if board[y][x] != ".":
                r = findFour(y, x, board[y][x])
                if len(r) > 0:
                    for rx in r:
                        check.add(rx)    
    for x in check:
        goDown(x)
        
    if len(check) == 0:
        break
    ans += 1
print(ans)