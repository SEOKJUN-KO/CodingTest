import sys
from collections import deque
import copy

N = int(sys.stdin.readline() )
minN = float('inf')
maxN = 0
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    minN = min(minN, min(board[i]))
    maxN = max(maxN, max(board[i]))

dx = [+0, +0, -1, +1]
dy = [-1, +1, +0, +0]

def BFS(x, y):
    global N
    que = deque()
    que.append([x, y])
    cpyBoard[y][x] = 0
    while(que):
        cx, cy = que.popleft()
        for i in range(4):
            X, Y = cx+dx[i], cy+dy[i]
            if( 0 <= X < N and 0 <= Y < N and cpyBoard[Y][X] != 0):
                cpyBoard[Y][X] = 0
                que.append([X, Y])

ans = 1
for i in range(minN, maxN+1):
    cnt = 0
    cpyBoard = copy.deepcopy(board)
    for y in range(N):
        for x in range(N):
            if(cpyBoard[y][x] <= i):
                cpyBoard[y][x] = 0
    for y in range(N):
        for x in range(N):
            if(cpyBoard[y][x] > i):
                BFS(x, y)
                cnt += 1
    ans = max(ans, cnt)
print(ans)
