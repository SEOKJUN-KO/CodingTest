import sys
input = sys.stdin.readline
N = int(input())

lines = []

for _ in range(N):
    s, e = map(int, input().split())
    lines.append([s, e])
lines = sorted(lines, key = lambda x: x[0] )
print(lines)
DP = [1]
for i in range(1, N):
    cnt = 0
    for j in range(i-1, -1, -1):
        if( lines[j][1] < lines[i][1] and cnt < DP[j]):
            cnt = DP[j]
    DP.append(cnt+1)
print(N-max(DP))
