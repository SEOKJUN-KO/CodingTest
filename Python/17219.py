import sys
N, M = map(int, sys.stdin.readline().split())
passD = {}
for _ in range(N):
    domain, pw = sys.stdin.readline().split()
    passD[domain] = pw

for _ in range(M):
    domain = sys.stdin.readline().strip()
    print(passD[domain])
