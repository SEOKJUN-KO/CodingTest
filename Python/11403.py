import sys

input = sys.stdin.readline

N = int(input())
edges = []
for _ in range(N):
    edges.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if(edges[j][i] == 1 and edges[i][k] == 1 and edges[j][k] == 0):
                edges[j][k] = 1
for i in range(N):
    print(" ".join(map(str, edges[i])))
