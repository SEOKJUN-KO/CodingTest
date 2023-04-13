import sys
import heapq
input = sys.stdin.readline
V, E = map( int, input().split() )
minL = [float('inf')]*(V+1)
K = int(input())
graph = [ [] for _ in range(V+1) ]

for _ in range(E):
    u, v, w = map(int, input().split() )
    graph[u].append([w, v])

print(graph)
heap = []
minL[K] = 0
heapq.heappush(heap, [0, K])
while(heap):
    w, n = heapq.heappop(heap)
    if(minL[n] == w):
        for edge in graph[n]:
            if(edge[0]+w < minL[ edge[1] ] ):
                minL[edge[1]] = edge[0]+w
                heapq.heappush(heap, [minL[edge[1]], edge[1]])
for a in minL[1:]:
    if(a == float('inf')):
        print("INF")
        continue
    print(a)
