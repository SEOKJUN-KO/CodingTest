import sys
input = sys.stdin.readline

K, N = map(int, input().split(" "))
arr = []
for _ in range(K):
    arr.append(int(input()))
arr = sorted(arr)
left, right = 0, 2**31-1
ans = 0
while(left <= right):
    mid = (left+right)//2
    cnt = 0
    for a in arr:
        cnt += a//mid
    if cnt < N:
        right = mid - 1
    elif cnt >= N:
        ans = max(mid, ans)
        left = mid + 1
print(ans)
