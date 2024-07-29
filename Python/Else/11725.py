import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
lList = [ set([]) for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    lList[v1].add(v2)
    lList[v2].add(v1)
p = [-1]*(N+1)
p[1] = 0

que = deque()
que.append(1)
while(que):
    V = que.popleft()
    for node in lList[V]:
        if(p[node] == -1):
            que.append(node)
            p[node] = V
for i in range(2, N+1):
    print(p[i])
