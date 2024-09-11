import sys; input = sys.stdin.readline
from heapq import heappush, heappop

N, M, K = map(int, input().split(" "))
graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    u, v, c = map(int, input().split(" "))
    graph[v].append([c, u])

interview = list(map(int, input().split(" ")))

que = []
minArr = [ float('inf') ]*(N+1)

for start in interview:
    heappush(que, [0, start])
    minArr[start] = 0
    
while(que):
    w, now = heappop(que)
    if minArr[now] < w: continue
    for c, nxt in graph[now]:
        if minArr[nxt] > w + c:
            minArr[nxt] = w + c
            heappush(que, [w+c, nxt])
far = 0; city = 1
for i in range(1, N+1):
    if i in interview: continue
    if minArr[i] > far:
        far = minArr[i]
        city = i
print(city)
print(far)
