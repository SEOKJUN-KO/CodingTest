import sys
from collections import deque
input=sys.stdin.readline

n,m,start=map(int,input().split())
visited=[False]*(n+1)

lList=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    lList[a].append(b)
    lList[b].append(a)
for i in range(1, n+1):
    lList[i] = sorted(lList[i])

def dfs(start):
    print(start,end=' ')
    visited[start]=True
    for i in lList[start]:
        if not visited[i]:
            dfs(i)
            visited[i]=True
            
def dfs(start):
    stack = [start]
    while(stack):
        n = stack.pop()
        if visited[n]:
            continue
        print(n,end=' ')
        A = []
        visited[n] = True
        for i in lList[n]:
            if not visited[i]:
                A.append(i)
        for a in A[::-1]:
            stack.append(a)

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in lList[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
dfs(start)
visited=[False]*(n+1)
print()
bfs(start)
