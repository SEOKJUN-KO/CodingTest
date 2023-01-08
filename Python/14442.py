import sys
from collections import deque

H, W, K = map(int, sys.stdin.readline().split())
board = []
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]

for _ in range(H):
    arr = []
    st = sys.stdin.readline().strip()
    for c in st:
        arr.append(int(c))
    board.append(arr)
    
dx = [+0, +0, -1, +1] # 상 하 좌 우
dy = [-1, +1, +0, +0]

def BFS():
    global W, H
    que = deque()
    que.append([0, 0, 0]) # x y t/f
    visited[0][0][0] = 1
    while(que):
        x, y, p = que.popleft()
        if( x == W-1 and y == H - 1 ):
            return visited[y][x][p]
        for i in range(4):
            X, Y = x+dx[i], y+dy[i]
            if( 0 <= X < W and 0 <= Y < H):
                if(p < K and board[Y][X] == 1 and visited[Y][X][p+1] == 0):
                    que.append([X, Y, p+1])
                    visited[Y][X][p+1] = visited[y][x][p] + 1
                elif(board[Y][X] == 0 and visited[Y][X][p] == 0):
                    que.append([X, Y, p])
                    visited[Y][X][p] = visited[y][x][p] + 1
    return -1
print(BFS())
