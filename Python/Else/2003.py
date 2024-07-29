N, M = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0

ans = 0
s = arr[0]
while(l <= r and l < N and r < N):
    if(s == M):
        ans += 1
        r += 1
        if(r == N):
            break
        s += arr[r]
    elif(l == r):
        r += 1
        if(r == N):
            break
        s += arr[r]
    elif(s > M):
        s -= arr[l]
        l += 1
    elif(s < M):
        r += 1
        if(r == N):
            break
        s += arr[r]
print(ans)
