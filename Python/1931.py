import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

brr = sorted(arr, key = lambda x: (x[1], x[0]))

m = 0
ans = 0
for b in brr:
    if(m <= b[0]):
        m = b[1]
        ans += 1
print(ans)
