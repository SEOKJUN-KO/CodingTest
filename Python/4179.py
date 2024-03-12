from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().split(" "))
JP = [-1, -1]
board = []
for _ in range(R):
    board.append(list(input().strip()))
que = deque()
for y in range(R):
    for x in range(C):
        if board[y][x] == 'F':
            que.append([x, y, 0])
            board[y][x] = -1
        elif board[y][x] == 'J':
            JP = [x, y]
            board[y][x] = float('inf')
        elif board[y][x] == '#':
            board[y][x] = -1
        elif board[y][x] == '.':
            board[y][x] = float('inf')
dx, dy = [-1, +1, +0, +0], [+0, +0, -1, +1]
while(que):
    x, y, t = que.popleft()
    for i in range(4):
        X, Y = x+dx[i], y+dy[i]
        if 0 <= X < C and 0 <= Y < R and board[Y][X] != -1:
            if board[Y][X] > t+1:
                board[Y][X] = t+1
                que.append([X, Y, t+1])

que.append([JP[0], JP[1], 0])
flag = False
while(que):
    x, y, t = que.popleft()
    for i in range(4):
        X, Y = x+dx[i], y+dy[i]
        if 0 <= X < C and 0 <= Y < R and board[Y][X] != -1:
            if board[Y][X] > t+1:
                board[Y][X] = t+1
                que.append([X, Y, t+1])
        elif not ( 0 <= X < C ) or not ( 0 <= Y < R ):
            flag = True
            print(t+1)
            break
    if flag: break
if not flag: print("IMPOSSIBLE")
