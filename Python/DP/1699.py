N = int(input())

DP = [0, 1, 2, 3, 1 ]
arr = [4]
for i in range( 5, N+1 ):
    if( int(i**(1/2)) == i**(1/2) ):
        DP.append(1)
        arr.append(i)
        continue
    ans = float('inf')
    for a in arr:
        ans = min(ans, DP[i-a]+1)
    DP.append(ans)
print(DP[N])
