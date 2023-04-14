import sys, heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1) ]
minL = [ float('inf') ]*(n+1)
preNode = [0]*(n+1)

for _ in range(m):
    s, e, w = map( int, input().split() )
    graph[s].append([w, e])
    
s, e = map( int, input().split() )
minL[s], preNode[s] = 0, s
heap = []
now = [0, s]
heapq.heappush( heap, now )
while(heap):
    now = heapq.heappop(heap)
    if(minL[now[1]] != now[0]): continue
    for edge in graph[now[1]]:
        if( minL[now[1]] + edge[0] >= minL[edge[1]] ): continue
        minL[edge[1]] = minL[now[1]] + edge[0]
        preNode[edge[1]] = now[1]
        heapq.heappush( heap, [ minL[edge[1]], edge[1]] )
print(minL[e])
ans = []
def findP(s, e):
    que = deque()
    que.append(e)
    ans.append(e)
    while(que):
        now = que.pop()
        if(now == s): break
        pre = preNode[now]
        que.append(pre)
        ans.append(pre)
findP(s, e)
print(len(ans))
print(" ".join(map(str, ans[::-1])))
