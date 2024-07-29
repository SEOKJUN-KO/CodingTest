import sys
input = sys.stdin.readline
N, K  = map(int, input().split() )
bags = []
for _ in range(N):
    bags.append(list(map(int, input().split())))
DP = [ [0]*(K+1) for _ in range(N+1) ]

for i in range(1, N+1):
    for j in range(1, K+1):
        if(j - bags[i-1][0] >= 0):
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-bags[i-1][0]] + bags[i-1][1])
        else:
            DP[i][j] = DP[i-1][j]
print(DP[-1][-1])
