import sys

input = sys.stdin.readline

N = int(input())
arr = [ 0 for _ in range(N+1) ]

ans = 0
for i in range(1, N+1):
    day, pay = map(int, input().split(" "))
    if (i+day <= N):
        arr[i+day] = max(arr[i+day], arr[i]+pay)
        if ans < arr[i+day]:
            ans = arr[i+day]
print(ans)