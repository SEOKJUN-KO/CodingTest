N = int(input())
if(N == 1):
    print(1)
    exit()
DP = [[0]*(2) for _ in range(N+1)]
DP[2] = [1, 0]
for i in range(3, N+1):
    DP[i][0], DP[i][1] = DP[i-1][0] + DP[i-1][1], DP[i-1][0]
print(sum(DP[N]))
