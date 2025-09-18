import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

board = []

def makeBoard(N):
    global board
    for _ in range(N):
        board.append(list(map(int, list(input().strip()))))

def bfs(N, M):
    global board
    que = deque()
    que.append([ False, 0, 0, set("0 0"), 1 ] )
    while(que):
        doBreak, ny, nx, passBy, w = que.popleft()
        for dy, dx in [ [-1, 0], [1, 0], [0, -1], [0, 1]]:
            Y, X = ny+dy, nx+dx
            key = str(Y)+" "+str(X)
            if ( 0 <= Y < N and 0 <= X < M and (key not in passBy) ):
                if (doBreak and board[Y][X] == 1): continue
                if ( Y == N-1 and X == M-1 ): return w+1

                S = deepcopy(passBy)
                S.add(key)
                if board[Y][X] == 1:
                    que.append( [True, Y, X, S, w+1])
                else:
                    que.append( [doBreak, Y, X, S, w+1])
    return -1

def solution():
    N, M = map(int, input().strip().split(" "))
    makeBoard(N)
    print(bfs(N, M))
    
solution()