import sys

input = sys.stdin.readline

def setInt():
    return int(input())

N = setInt()

arr = []
for _ in range(N):
    arr.append(setInt())
dp = [[0, 0], [arr[0], arr[0]]]

for n in arr[1:]:
    a = dp[-1][1] + n
    b = max(dp[-2]) + n
    dp.append([a, b])

print(max(dp[-1]))