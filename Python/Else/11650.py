import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
ans = sorted(arr, key = lambda x: (x[0], x[1]))
for a in ans:
    print(" ".join(map(str, a)))
