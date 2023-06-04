import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    row = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split())))
    DP = [ [0, 0, 0] for _ in range(row)]
    DP[0][0], DP[0][1], DP[0][2] = board[0][0], board[1][0], 0
    for r in range(1, row):
        f = max(DP[r-1][1], DP[r-1][2]) + board[0][r]
        t = max(DP[r-1][0], DP[r-1][2]) + board[1][r]
        th = max( DP[r-1][0], DP[r-1][1], DP[r-1][2] )
        DP[r] = [f,t,th]
    print(max(DP[-1]))
