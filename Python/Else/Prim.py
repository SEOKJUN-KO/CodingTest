import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
lList = [[] for _ in range(V+1)]
MST = [False]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    lList[u].append([w, v])
    lList[v].append([w, u])

MST[1] = True
heap = []
ans = []
for n in lList[1]:
    heapq.heappush(heap, n)

while(heap and len(ans) < V):
    w, v = heapq.heappop(heap)
    if(MST[v] == False):
        MST[v] = True
        ans.append(w)
        for info in lList[v]:
            if(MST[info[1]] == True):
                continue
            heapq.heappush(heap, info)
print(sum(ans))
