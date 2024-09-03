import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
graphA = [ [0]*(N+1) for _ in range(N+1) ]
graphB = [ [0]*(N+1) for _ in range(N+1) ]
for _ in range(M):
    A, B = map(int, input().split(" "))
    graphA[A][B] = 1
    graphB[B][A] = 1
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graphA[i][j] == 0 and graphA[i][k] == 1 and graphA[k][j] == 1: graphA[i][j] = 1
            if graphB[i][j] == 0 and graphB[i][k] == 1 and graphB[k][j] == 1: graphB[i][j] = 1
ans = 0
for y in range(1, N+1):
    A = sum(graphA[y])
    B = sum(graphB[y])
    if A >= (N+1)/2 or B >= (N+1)/2: ans += 1
print(ans)
