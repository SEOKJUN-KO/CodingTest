import sys
from collections import deque

H, W, K = map( int, sys.stdin.readline().split() )
board = [[0]*W for _ in range(H)]

for _ in range(K):
    lbx, lby, rux, ruy = map( int, sys.stdin.readline().split() )
    for y in range(lby, ruy):
        for x in range(lbx, rux):
            board[H-y-1][x] = 1 # 4 - 2 + 1
            
dx = [+0, +0, -1, +1]
dy = [-1, +1, +0, +0]
def BFS(x, y):
    global W, H
    que = deque()
    que.append([x, y])
    board[y][x] = 1
    cnt = 1
    while(que):
        cx, cy = que.popleft()
        for i in range(4):
            X, Y = cx+dx[i], cy+dy[i]
            if( 0 <= X < W and 0 <= Y < H and board[Y][X] == 0):
                board[Y][X] = 1
                cnt += 1
                que.append([X, Y])
    return cnt

ans = []
for y in range(H):
    for x in range(W):
        if(board[y][x] == 0):
            ans.append(BFS(x, y))
print(len(ans))
print(" ".join((str (c) for c in sorted(ans))))
