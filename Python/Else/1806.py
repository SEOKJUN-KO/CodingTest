N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
ans = float('inf')
sumA = arr[0]
if(sumA >= M):
    print(1)
    exit()
while(True):
    if(sumA < M):
        e += 1
        if(e==N): break
        sumA += arr[e]
    else:
        if(ans > e-s+1):
            ans = e-s+1
        sumA -= arr[s]
        s += 1
        if(s > e): break
        
if(ans == float('inf')):
    print(0)
else:
    print(ans)
