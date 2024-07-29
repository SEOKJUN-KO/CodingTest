import sys
from collections import deque

dx = [-2, -2, -1, -1, +1, +1, +2, +2]
dy = [-1, +1, -2, +2, -2, +2, -1, +1]

for _ in range(int(sys.stdin.readline())):
    I = int(sys.stdin.readline())
    board = [[0]*I for _ in range(I)]
    # print(board)
    cx, cy = map(int, sys.stdin.readline().split() )
    tx, ty = map(int, sys.stdin.readline().split() )
    que = deque()
    que.append([cx, cy, 0])
    board[cy][cx] = 1
    while(que):
        x, y, w = que.popleft()
        if(x == tx and y == ty):
            print(w)
            break
        for i in range(8):
            X, Y = x+dx[i], y+dy[i]
            if(0 <= X < I and 0 <= Y < I and board[Y][X] == 0):
                board[Y][X] = 1
                que.append([X, Y, w+1])
