# r.logr
from collections import deque

def solution(n, roads, sources, destination):
    ans = []
    maps = [ [] for _ in range(n+1) ]
    for n1, n2 in roads:
        maps[n1].append(n2)
        maps[n2].append(n1)
    que = deque()
    visit = [float('inf')] * (n+1)
    que.append([destination, 0])
    visit[destination] = 0
    while(que):
        now, weight = que.popleft()
        if visit[now] != weight: continue
        for node in maps[now]:
            if visit[node] > weight+1:
                visit[node] = weight+1
                que.append([node, weight+1])
    for s in sources:
        if visit[s] == float('inf'): ans.append(-1)
        else: ans.append(visit[s])
    return ans
