import bisect

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        target = -(a[i] + a[j])
        left = bisect.bisect_left(a, target, j + 1, n)
        right = bisect.bisect_right(a, target, j + 1, n)
        ans += right - left

print(ans)