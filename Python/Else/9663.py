from collections import deque
N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

isUsed = [False]*40 # 세로
isUsed2 = [False]*40 # 대각선 /
isUsed3 = [False]*40 # 대각선 \

ans = 0
def backtracking(y):
    global ans, c, N
    if(y == N):
        ans += 1
        return
    for x in range(N):
        if( isUsed[x] or isUsed2[x+y] or isUsed3[x-y+N-1]):
            continue
        isUsed[x] = True
        isUsed2[x+y] = True
        isUsed3[x-y+N-1] = True
        backtracking(y+1)
        isUsed[x] = False
        isUsed2[x+y] = False
        isUsed3[x-y+N-1] = False
        
backtracking(0)
print(ans)
