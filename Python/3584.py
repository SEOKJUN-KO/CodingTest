import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    graph = [ 0 for _ in range(N+1) ]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[b] = a
    visited = [0]*(N+1)
    visited[0] = -1
    que = deque()
    A, B = map(int, input().split())
    que.append([A, 1])
    visited[A] = 1
    que.append([B, 2])
    visited[B] = 2
    while(que):
        now, mode = que.popleft()
        node = graph[now]
        if(visited[node] == -1): continue
        if(visited[node] == 0):
            visited[node] = mode
            que.append([node, mode])
        elif(visited[node] != mode):
            print(node)
            break
