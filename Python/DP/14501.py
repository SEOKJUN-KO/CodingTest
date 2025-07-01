import sys

input = sys.stdin.readline

N = int(input())
arr = [ 0 for _ in range(N+2) ]

ans = 0
for i in range(1, N+1):
    day, pay = map(int, input().split(" "))
    for j in range(i-1, -1, -1):
        arr[i] = max(arr[j], arr[i])
    if (i+day <= N+1):
        arr[i+day] = max(arr[i+day], arr[i]+pay)
        if ans < arr[i+day]:
            ans = arr[i+day]
    
print(arr[1:])
print(ans)