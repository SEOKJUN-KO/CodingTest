import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
hall = [ [0]*(M) for _ in range(N) ]
for _ in range(K):
    r, c = map(int, input().split())
    hall[r-1][c-1] = 1

dx = [+0, +0, -1, +1] # 상, 하, 좌, 우
dy = [-1, +1, +0, +0]

def BFS():
    size = 1
    while(que):
        nx, ny = que.popleft()
        for i in range(4):
            X, Y = nx+dx[i], ny+dy[i]
            if(0<=X<M and 0<=Y<N and hall[Y][X] == 1):
                hall[Y][X] = 0
                que.append([X, Y])
                size += 1
    return size

ans = 0
for y in range(N):
    for x in range(M):
        if(hall[y][x] == 1):
            que = deque()
            que.append([x, y])
            hall[y][x] = 0
            size = BFS()
            if(ans < size):
                ans = size
print(ans)
