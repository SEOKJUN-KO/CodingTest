n = int(input())
jumps = list(map(int, input().split() ))

DP = [float('inf')]*(n)
DP[0] = 0
for i in range(0, n):
    if( jumps[i] == 0 ):
        continue
    for j in range(i+1, i+jumps[i]+1):
        if(j >= n):
            break
        if( DP[i]+1 < DP[j] ):
            DP[j] = DP[i]+1
if(DP[-1] == float('inf')):
    print(-1)
else:
    print(DP[-1])
