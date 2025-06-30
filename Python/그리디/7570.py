import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

store = [0 for _ in range(N+1)]

cnt = 0
for a in arr:
    store[a] += store[a-1] + 1
    if cnt < store[a]:
        cnt = store[a]

print(N-cnt)