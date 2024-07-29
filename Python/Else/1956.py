import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [ [float('inf')]*(V+1) for _ in range(V+1) ]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if( graph[i][j] > graph[i][k] + graph[k][j] ):
                graph[i][j] = graph[i][k] + graph[k][j]
ans = float('inf')
for i in range(1, V+1):
    if( graph[i][i] < ans ):
        ans = graph[i][i]
if(ans == float('inf') ):
    print(-1)
else:
    print(ans)
