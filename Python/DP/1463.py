N = int(input())
dp = [ 99999999 for _ in range(N+1)]
dp[1] = 0

i = 1
while(True):
    for a in [ i+1, i*2, i*3 ]:
        n = dp[i]+1
        if a <= N and dp[a] > n:
            dp[a] = n
        if a == N:
            break
    i += 1
    if i > N: break
print(dp[N])