import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
ans = [[], 0]
for i in range(1, N+1):
    leng = [0]*(N+1)
    que = deque()
    que.append(i)
    while(que):
        now = que.popleft()
        for e in graph[now]:
            if(leng[e] == 0 and e != i):
                leng[e] = 1
                que.append(e)
    if(sum(leng) > ans[1]):
        ans[0], ans[1] = [i], sum(leng)
    elif(sum(leng) == ans[1]):
        ans[0].append(i)
print(" ".join(map(str, ans[0])))
