import sys
input = sys.stdin.readline

N = int(input())
board = []
board.append(list(map(int, input().split())))
board[0] = [ [board[0][0], board[0][0]] , [board[0][1], board[0][1]], [board[0][2], board[0][2]] ]

for _ in range(1, N):
    A, B, C = map(int, input().split())
    D = [ max(board[0][0][0], board[0][1][0]) + A, min(board[0][0][1], board[0][1][1]) + A ]
    E = [ max(board[0][0][0], board[0][1][0], board[0][2][0]) + B, min(board[0][0][1], board[0][1][1], board[0][2][1]) + B ]
    F = [ max(board[0][1][0], board[0][2][0]) + C, min(board[0][1][1], board[0][2][1]) + C ]
    board[0] = [D, E, F]
print( max(board[0][0][0], board[0][1][0], board[0][2][0]), min(board[0][0][1], board[0][1][1], board[0][2][1]) )
