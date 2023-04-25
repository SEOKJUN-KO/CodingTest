import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [ [float('inf')]*(N+1) for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for s in range(1, N+1):
    for m in range(1, N+1):
        for e in range(1, N+1):
            if( s != e and graph[s][e] > graph[s][m] + graph[m][e] ):
                graph[s][e] = graph[s][m] + graph[m][e]
            elif(s == e):
                graph[s][e] = 0
ans = 1
f = float('inf')
for i in range(1, N+1):
    if(f > sum( graph[i][1:]) ):
        f = sum( graph[i][1:] )
        ans = i
print(ans)            
