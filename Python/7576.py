from collections import deque
import sys

W, H = map(int, sys.stdin.readline().split() )
board = []
for i in range(H):
    board.append( list(map(int, sys.stdin.readline().split() )) )

dx = [+0, +0, -1, +1] # 상, 하, 좌, 우
dy = [-1, +1, +0, +0]

def BFS():
    global W, H
    m = 0
    while(que):
        cx, cy, w = que.popleft()
        m = max(m, w)
        for i in range(4):
            X, Y = cx+dx[i], cy+dy[i]
            if( 0 <= X < W and 0 <= Y < H and board[Y][X] == 0):
                board[Y][X] = 1
                que.append([X, Y, w+1])
    return m

que = deque()
for y in range(H):
    for x in range(W):
        if(board[y][x] == 1):
            que.append([x, y, 0])
A = BFS()
for y in range(H):
    for x in range(W):
        if(board[y][x] == 0):
            print(-1)
            exit()
print(A)
