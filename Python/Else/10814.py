import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    ages, name = sys.stdin.readline().split()
    arr.append([int(ages), name])
ans = sorted(arr, key = lambda x: x[0])
for a in ans:
    print(" ".join(map(str, a)) )
