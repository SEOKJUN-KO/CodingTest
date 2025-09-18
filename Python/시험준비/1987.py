import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

board = []

def makeBoard(N):
    global board
    for _ in range(N):
        board.append(list(input().strip()))

ans = 1
def dfs(N, M, ny, nx, passBy):
    global board, ans

    if ans == 26: return

    for dy, dx in [ [-1, 0], [1, 0], [0, -1], [0, 1]]:
        Y, X = ny+dy, nx+dx
        if not (0 <= Y < N and 0 <= X < M): continue
        key = board[Y][X]
        if ( key not in passBy ):
            passBy.add(key)
            if ans < len(passBy): ans = len(passBy)
            dfs(N, M, Y, X, passBy)
            passBy.remove(key)
        
    return ans

def solution():
    global board, ans 
    N, M = map(int, input().strip().split(" "))
    makeBoard(N)
    dfs(N, M, 0, 0, set(board[0][0]))
    print(ans)
    
solution()