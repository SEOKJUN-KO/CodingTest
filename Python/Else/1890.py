import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
boards = []
for _ in range(N):
    boards.append(list(map(int, input().split())))

DP = [ [0]*N for _ in range(N) ]
DP[0][0] = 1
for y in range(N):
    for x in range(N):
        if(x == N-1 and y == N-1):
            break
        if(DP[y][x] > 0):
            X, Y = x+boards[y][x], y+boards[y][x]
            if(0 <= X < N):
                DP[y][X] += DP[y][x]
            if(0 <= Y < N):
                DP[Y][x] += DP[y][x]
print(DP[-1][-1])
