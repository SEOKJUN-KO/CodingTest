from collections import deque
import sys
dx = [+0, +0, -1, +1] # 상, 하, 좌, 우
dy = [-1, +1, +0, +0]

H, W = map(int, sys.stdin.readline().split())
board = []
for _ in range(H):
    board.append( list(map(int, sys.stdin.readline().split())) )

def BFS(x, y):
    global W, H
    mw = 1
    que = deque()
    board[y][x] = 0
    que.append([x, y])
    while(que):
        px, py = que.popleft()
        for i in range(4):
            X, Y = px+dx[i], py+dy[i]
            if( 0 <= X < W and 0 <= Y < H and board[Y][X] == 1):
                board[Y][X] = 0
                mw += 1
                que.append([X, Y])
    return mw

w = 0
c = 0
for y in range(H):
    for x in range(W):
        if(board[y][x] == 1):
            c += 1
            w = max(w, BFS(x, y))
print(c)
print(w)
