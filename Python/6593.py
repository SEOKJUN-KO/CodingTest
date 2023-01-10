import sys
from collections import deque

dx = [-1, +1, +0, +0, +0, +0]
dy = [+0, +0, -1, +1, +0, +0]
dz = [+0, +0, +0, +0, -1, +1]
def BFS():
    global sz, sy, sx, ez, ey, ex, Z, Y, X
    que = deque()
    que.append([sx, sy, sz, 0])
    board[sz][sy][sx] = '#'
    while(que):
        x, y, z, w = que.popleft()
        for i in range(6):
            cx, cy, cz = x+dx[i], y+dy[i], z+dz[i]
            if( 0 <= cx < X and 0 <= cy < Y and 0 <= cz < Z and board[cz][cy][cx] != "#"):
                if(board[cz][cy][cx] == "E"):
                    return w+1
                board[cz][cy][cx] = '#'
                que.append([cx, cy, cz, w+1])
    return -1
    
Z, Y, X = map(int, sys.stdin.readline().split())
while(Z != 0 and Y != 0 and X != 0):
    board = []
    sz, sy, sx = 0, 0, 0
    ez, ey, ex = 0, 0, 0
    for z in range(Z):
        arr = []
        j = 0
        st = sys.stdin.readline().strip()
        while(st != "\n".strip()):
            ar = []
            i = 0
            for c in st:
                if(c == 'S'):
                    sz, sy, sx = z, j, i
                if(c == 'E'):
                    ez, ey, ex = z, j, i
                i += 1
                ar.append(c)
            arr.append(ar)
            j += 1
            st = sys.stdin.readline().strip()
        board.append(arr)

    A = BFS()
    if(A == -1):
        print("Trapped!")
    else:
        print("Escaped in "+str(A)+" minute(s).")
    Z, Y, X = map(int, sys.stdin.readline().split())
