n = int(input())
arr = list(map(int, input().split()))

DP = [arr[0]]
for i in range(1, n):
    l, r, m = 0, i-1, 0
    while(l <= r):
        if(m < DP[l]+DP[r]):
            m = DP[l]+DP[r]
        l += 1
        r -= 1
    if(m > arr[i]):
        DP.append(m)
    else:
        DP.append(arr[i])
print(DP[-1])
