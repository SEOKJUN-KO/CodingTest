import sys
input = sys.stdin.readline
N = int(input())
color = []
color.append(list(map(int, input().split())))
for i in range(1, N):
    color.append(list(map(int, input().split())))
    color[i][0] += min(color[i-1][1], color[i-1][2])
    color[i][1] += min(color[i-1][0], color[i-1][2])
    color[i][2] += min(color[i-1][0], color[i-1][1])

print(min(color[N-1]))
