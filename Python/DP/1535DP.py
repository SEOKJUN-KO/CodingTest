N = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

DP = [ [0]*(101) for _ in range(N+1) ]

for i in range(1, N+1):
    for j in range(1, 101):
        if(j - hp[i-1] > 0):
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-hp[i-1]] + happy[i-1])
        else:
            DP[i][j] = DP[i-1][j]
if(N == 0):
    print(0)
else:
    print(DP[-1][100])
