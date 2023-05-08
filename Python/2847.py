import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
ans = 0
arr = arr[::-1]
for i in range(len(arr)-1):
    if(arr[i] <= arr[i+1]):
        ans += (arr[i+1] - (arr[i] - 1))
        arr[i+1] = arr[i] - 1
print(ans)
