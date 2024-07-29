from collections import deque
import sys

H, W = map(int, sys.stdin.readline().split() )
board = []
for i in range(H):
    st = sys.stdin.readline().strip()
    arr = []
    for c in st:
        arr.append(int(c))
    board.append(arr)

dx = [+0, +0, -1, +1] # 상, 하, 좌, 우
dy = [-1, +1, +0, +0]

def BFS():
    global W, H
    que = deque()
    que.append([0, 0, 1])
    board[0][0] = 0
    while(que):
        cx, cy, w = que.popleft()
        for i in range(4):
            X, Y = cx+dx[i], cy+dy[i]
            if( 0 <= X < W and 0 <= Y < H and board[Y][X] == 1):
                board[Y][X] = 0
                if(X == W-1 and Y == H-1):
                    return w+1
                que.append([X, Y, w+1])

print(BFS())
