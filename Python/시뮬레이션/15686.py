import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split(" "))

board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))
house = []
chicken = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            house.append([y, x])
        elif board[y][x] == 2:
            chicken.append([y, x])

arr = []
visit = [False]*(len(chicken))
ans = float('inf')
def backTracking(start):
    global ans
    if len(arr) == M:
        tmp = [float('inf')]*(len(house))
        for a in arr:
            for j in range(len(house)):
                tmp[j] = min(tmp[j], abs(house[j][0]-a[0])+abs(house[j][1]-a[1]))
        ans = min(ans, sum(tmp))
        return
    for i in range(start, len(chicken)):
        if not visit[i]:
            visit[i] = True
            arr.append(chicken[i])
            backTracking(i+1)
            arr.pop()
            visit[i] = False
backTracking(0)
print(ans)
