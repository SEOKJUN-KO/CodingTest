import sys
input = sys.stdin.readline
from collections import deque

def makeBoard(N, M):
    board = []
    for _ in range(N):
        arr = list(map(int, input().split(" ")))
        board.append(arr)
    return board

def calculate(board, D, N, M, y, x):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0
    arr = []
    for i in range(4):
        Y, X = y+dy[i], x+dx[i]
        if 0 <= Y < N and 0 <= X < M:
            if board[Y][X] > board[y][x]:
                if D[Y][X] == -1:
                    return [-1]
                cnt += D[Y][X]
            elif board[Y][X] < board[y][x]:
                arr.append([Y, X])
    arr.append(cnt)
    return arr

            

def DP(board, N, M):
    que = deque()
    D = [ [ -1 for _ in range(M) ] for _ in range(N) ]
    D[0][0] = 1
    if M >= 2:
        que.append([0, 1])
    if N >= 2:
        que.append([1, 0])
    for y in range(N): # 500*500*4
        for x in range(M):
            if D[y][x] == -1:
                arr = calculate(board, D, N, M, y, x)
                if arr[-1] != -1:
                    D[y][x] = arr[-1]
                    for a in arr[:len(arr)-1]:
                        que.append(a)

    while(que):
        y, x = que.popleft()
        if D[y][x] != -1: continue
        arr = calculate(board, D, N, M, y, x)
        if arr[-1] != -1:
            D[y][x] = arr[-1]
            for a in arr[:len(arr)-1]:
                que.append(a)
    return D[-1][-1]

def main():
    N, M = map(int, input().split(" "))
    board = makeBoard(N, M)
    ans = DP(board, N, M)
    print(ans)
main()