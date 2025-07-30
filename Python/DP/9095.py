import sys
dp = [1, 2, 4]

input = sys.stdin.readline

m = 0
arr = []
for _ in range(int(input())):
    n = int(input())
    arr.append(n)
    m = max(n, m)

for i in range(3, m+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for a in arr:
    print(dp[a-1])