import sys

input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for h in range(n-1, 0, -1):
    for i in range(h):
        arr[h-1][i] += max(arr[h][i], arr[h][i+1])
print(arr[0][0])
