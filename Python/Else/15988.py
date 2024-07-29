import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input()))
M = max(arr)
DP = [0]*(M+1)
DP[1], DP[2], DP[3] = 1, 2, 4
for i in range(4, M+1):
    DP[i] = (DP[i-1]+DP[i-2]+DP[i-3])%1000000009
for a in arr:
    print(DP[a])
