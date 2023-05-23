N, K = map(int, input().split() )
arr = list(map(int, input().split()))
isUsed = [False]*(N)
ans = 0

def backT(deep, total):
    global N, K, ans
    if(deep >= N):
        ans += 1
        return
    for i in range(N):
        if(isUsed[i] == False):
            isUsed[i] = True
            total -= K
            total += arr[i]
            if(total >= 0):
                backT(deep+1, total)
            total -= arr[i]
            total += K
            isUsed[i] = False
backT(0, 0)
print(ans)
