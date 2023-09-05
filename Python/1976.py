import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = []
for i in range(n): graph.append(list(map(int, input().split())))
for i in range(n): graph[i][i] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == 0 and graph[i][k] == 1 and graph[k][j] == 1): graph[i][j] = 1
visit = list(map(int, input().split()))

now = visit[0]
for i in range(1, m):
    target = visit[i]
    if(graph[now-1][target-1] == 0): 
        print("NO")
        exit()
    now = target
print("YES")
