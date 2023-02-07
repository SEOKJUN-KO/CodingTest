import sys

N = int(sys.stdin.readline())
arr = []
mx = 0
for _ in range(N):
    A = int(sys.stdin.readline())
    arr.append(A)
    mx = max(mx, A)
DP = [0]*(mx+1)
if(mx < 3):
    DP = [0]*(4)
DP[1] = 1
DP[2] = 1
DP[3] = 1
for i in range(4, mx+1):
    DP[i] = DP[i-2] + DP[i-3]
for a in arr:
    print(DP[a])
