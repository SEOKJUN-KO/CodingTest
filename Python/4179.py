from collections import deque
import sys

H, W = map(int, sys.stdin.readline().split() )
board = []
jx, jy = 0, 0
for i in range(H):
    st = sys.stdin.readline().strip()
    arr = []
    j = 0
    for c in st:
        if(c == "."):
            arr.append(0)
        elif(c == 'F'):
            arr.append(1001)
        elif(c == 'J'):
            jy = i
            jx = j
            if(i == 0 or i == H-1 or j == 0 or j == W-1):
                print(1)
                exit()
            arr.append(1002)
        else:
            arr.append(-1)
        j += 1
    board.append(arr)

dx = [+0, +0, -1, +1] # 상, 하, 좌, 우
dy = [-1, +1, +0, +0]

# Fire
def BFS():
    global W, H
    while(que):
        cx, cy, w = que.popleft()
        for i in range(4):
            X, Y = cx+dx[i], cy+dy[i]
            if( 0 <= X < W and 0 <= Y < H and board[Y][X] == 0 ):
                board[Y][X] = w + 1
                que.append([X, Y, w+1])

que = deque()
for y in range(H):
    for x in range(W):
        if(board[y][x] == 1001):
            que.append([x, y, 0])
BFS()

# Jihun
que = deque()
que.append([jx, jy, 1])
def BFSJ():
    global W, H
    while(que):
        cx, cy, w = que.popleft()
        for i in range(4):
            X, Y = cx+dx[i], cy+dy[i]
            if( 0 <= X < W and 0 <= Y < H and ( board[Y][X] > w or board[Y][X] == 0 ) ):
                if( X == 0 or X == W-1 or Y == 0 or Y == H-1):
                    return w+1
                board[Y][X] = -1
                que.append([X, Y, w+1])
    return -4
A = BFSJ()
if(A == -4):
    print("IMPOSSIBLE")
else:
    print(A)
