import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

DP = [0]*(k+1)
DP[0] = 1
for i in range(n):
    for j in range(coins[i], k+1):
        DP[j] += DP[j-coins[i]]
print(DP[-1])
