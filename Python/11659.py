import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
DP = [0]*(N+1)
DP[1] = sum(arr)

for i in range(2, N+1):
    DP[i] = DP[i-1] - arr[i-2]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(DP[A]-DP[B]+arr[B-1])
