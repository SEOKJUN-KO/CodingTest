N = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr = sorted(arr)
brr = sorted(brr, key = lambda x: -x)

ans = 0
for i in range(N):
    ans += arr[i]*brr[i]
print(ans)
