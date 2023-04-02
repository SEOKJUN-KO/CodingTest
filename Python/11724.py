import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
A = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    V1, V2 = map(int, sys.stdin.readline().split())
    A[V1][V2] = 1
    A[V2][V1] = 1

def checkConnected(V):
    que = deque()
    que.append(V)
    visited[V] = True
    while(que):
        now = que.popleft()
        for v in range(1, N+1):
            if(A[now][v] == 1 and visited[v] == False):
                visited[v] = True
                que.append(v)
ans = 0
for i in range(1, N+1):
    if(visited[i] == False):
        checkConnected(i)
        ans += 1
print(ans)
