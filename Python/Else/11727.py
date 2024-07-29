N = int(input())
DP = [0]*(N+1)
DP[1] = 1
if(N>=2):
    DP[2] = 3
    for i in range(3, N+1):
        DP[i] = (DP[i-1] + 2*DP[i-2])%10007
print(DP[N])
