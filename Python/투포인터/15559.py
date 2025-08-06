import sys
input = sys.stdin.readline
from collections import deque

used = {}
def makeBoard(N):
    board = []
    for _ in range(N):
        board.append( list(input().strip()))
    return board

def isHereCame(y, x):
    global used
    if y not in used.keys():
        return False
    if (used[y] & (1 << x)) == 0:
        return False
    return True

def goThere(y, x):
    global used
    used[y] = used[y] | (1 << x)

def check(board, N, M, y, x):
    global used
    
    d = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}
    que = deque()
    que.append([y, x])
    while(que):
        Y, X = que.popleft()
        if isHereCame(Y, X): continue
        if Y not in used.keys(): used[Y] = 0
        goThere(Y, X)
        dy, dx = d[board[Y][X]]
        que.append([Y+dy, X+dx])
        if 0 <= Y-1 < N and 0 <= X < M and board[Y-1][X] == "S": que.append([Y-1, X])
        if 0 <= Y+1 < N and 0 <= X < M and board[Y+1][X] == "N": que.append([Y+1, X])
        if 0 <= Y < N and 0 <= X-1 < M and board[Y][X-1] == "E": que.append([Y, X-1])
        if 0 <= Y < N and 0 <= X+1 < M and board[Y][X+1] == "W": que.append([Y, X+1])

    return

def calculate(board, N, M):
    ans = 0
    global used
    for y in range(N):
        for x in range(M):
            if not isHereCame(y, x):
                ans += 1
                check(board, N, M, y, x)

    return ans

def main():
    N, M = map(int, input().split(" "))
    board = makeBoard(N)
    print(calculate(board, N, M))
    return

main()