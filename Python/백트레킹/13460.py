import sys
from copy import deepcopy 
input = sys.stdin.readline

ans = 11
arr = []
p = {'R': [0, 0], 'B': [0, 0]}
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def makeBoard(N):
    board = []
    for _ in range(N):
        arr = list(input().strip())
        board.append(arr)
    return board

def findRedBlue(board, N, M):
    global p
    for y in range(N):
        for x in range(M):
            if board[y][x] == "R":
                p['R'] = [y, x]
            elif board[y][x] == "B":
                p['B'] = [y, x]

def moveMarble(board, N, M, i, key):
    global p, dy, dx
    y, x = p[key]
    Y, X = y+dy[i], x+dx[i]
    if not(0 <= Y < N and 0 <= X < M): # 움직일 수 있는 범위 벗어남
        return "can't move"
    if board[Y][X] == "#": # 막힘
        return "can't move"
    elif board[Y][X] == "R" or board[Y][X] == "B": # 구슬이 존재
        return "can't move"
    elif board[Y][X] == ".": # 빈칸
        board[Y][X] = key
        p[key] = [Y, X]
        board[y][x] = "."
        return "moved"
    elif board[Y][X] == "O" and key == "R": # 빨간 구슬 들어감
        board[y][x] = "."
        return "win"
    elif board[Y][X] == "O" and key == "B": # 파란 구슬 들어감
        return "fail"

    return

def moveOneDirection(board, N, M, i, level):
    global ans
    while(True):
        R = moveMarble(board, N, M, i, 'R')
        B = moveMarble(board, N, M, i, 'B')
        if R == "moved" or B == "moved": continue # 둘중에 하나라도 움직임
        if B == "fail":
            return "fail"
        if R == "win":
            if ans > level: ans = level
            return "win"
        if R == "can't move" and B == "can't move": # 움직일 수 없기 때문
            break
    return "can't move"

def cleanUp(board, exRed, exBlue):
    global p
    nRy, nRx = p["R"]
    nBy, nBx = p["B"]
    board[nRy][nRx] = "."
    board[nBy][nBx] = "."

    exRy, exRx = exRed
    exBy, exBx = exBlue
    board[exRy][exRx] = "R"
    board[exBy][exBx] = "B"
    p["R"] = exRed
    p["B"] = exBlue

def backtracking(board, N, M, level):
    global ans, p, dy, dx, arr
    if level >= 11 or level >= ans:
        return False
    
    for i in range(4):
        exRedPosition = deepcopy(p["R"])
        exBluePosition = deepcopy(p["B"])
        status = moveOneDirection(board, N, M, i, level)
        if status == "can't move":
            if exRedPosition != p["R"] or exBluePosition != p["B"]:
                backtracking(board, N, M, level+1)
        else:
            cleanUp(board, exRedPosition, exBluePosition)
            if status == "win": return True

        cleanUp(board, exRedPosition, exBluePosition)
    
    return False

def main():
    global ans, p
    N, M = map(int, input().split(" "))
    board = makeBoard(N)
    findRedBlue(board, N, M)
    backtracking(board, N, M, 1)
    if ans == 11: print(-1)
    else:print(ans)

    
main()