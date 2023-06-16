import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
leng = [0]*(N+1)
que = deque()
que.append(1)
while(que):
    now = que.popleft()
    for e in graph[now]:
        if(leng[e] == 0 and e != 1):
            leng[e] = leng[now]+1
            que.append(e)
maxL = max(leng)
ans = [0, 0, 0]
for i in range(1, N+1):
    if(ans[1]<leng[i]):
        ans[0] = i
        ans[1] = leng[i]
        ans[2] = 1
    elif(ans[1] == leng[i]):
        ans[2] += 1
print(" ".join(map(str,ans)))
