import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
boards = []
for _ in range(N):
    boards.append( list(map(int, input().split(" "))) )

for k in range(N):
    for i in range(N):
        for j in range(N):
            if(boards[i][j] > boards[i][k] + boards[k][j] ):
                boards[i][j] = boards[i][k] + boards[k][j]

for _ in range(M):
    start, target, time = map(int, input().split())
    if(boards[start-1][target-1] > time):
        print("Stay here")
    else:
        print("Enjoy other party")
