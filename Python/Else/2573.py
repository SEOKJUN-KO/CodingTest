import sys
from collections import deque
import copy

H, W = map(int, sys.stdin.readline().split())
board = []
for _ in range(H):
    board.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, +1, +0, +0]
dy = [+0, +0, -1, +1]

def BFS(x, y):
    global W, H
    que = deque()
    que.append([x, y])
    copyB[y][x] = 0
    while(que):
        cx, cy = que.popleft()
        for i in range(4):
            X, Y = cx+dx[i], cy+dy[i]
            if( 0 <= X < W and 0 <= Y < H and copyB[Y][X] != 0):
                copyB[Y][X] = 0
                que.append([X, Y])
year = 0
while(True):
    s = 0
    for y in range(H):
        s += sum(board[y])
        for x in range(W):
            if(board[y][x] != 0):
                c = 0
                for i in range(4):
                    X, Y = x+dx[i], y+dy[i]
                    if( 0 <= X < W and 0 <= Y < H and board[Y][X] == 0):
                        c += 0.1
                board[y][x] += c
    if(s == 0):
        print(0)
        exit()
    for y in range(H):
        for x in range(W):
            if(board[y][x] != 0):
                board[y][x] = int( board[y][x] - int(board[y][x]*10%10 ) )
                if(board[y][x] < 0):
                    board[y][x] = 0
    copyB = copy.deepcopy(board)
    cnt = 0
    year += 1
    for y in range(H):
        for x in range(W):
            if(copyB[y][x] != 0):
                cnt += 1
                BFS(x, y)
    if( cnt >= 2 ):
        print(year)
        exit()
