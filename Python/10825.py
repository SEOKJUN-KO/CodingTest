import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().split())
ans = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for a in ans:
    print(a[0])
