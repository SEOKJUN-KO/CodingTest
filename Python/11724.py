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

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

visited = [False]*(N+1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LList:
    def __init__(self):
        self.head = None
    def addFirst(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    def mprint(self):
        node = self.head
        while node is not None:
            print(node.val, end=" ")
            node = node.next
    def searchNode(self):
        node = self.head
        while node is not None:
            if(visited[node.val] == False):
                visited[node.val] = True
                return node.val
            node = node.next
        return 0
A = [LList() for _ in range(N+1)]

for j in range(M):
    V1, V2 = map(int, sys.stdin.readline().split())
    A[V1].addFirst(V2)
    A[V2].addFirst(V1)

def checkConnected(V):
    que = deque()
    que.append(V)
    visited[V] = True
    while(que):
        now = que.popleft()
        while(True):
            O = A[now].searchNode()
            if(O == 0):
                break
            que.append(O)
ans = 0
for i in range(1, N+1):
    if(visited[i] == False):
        checkConnected(i)
        ans += 1
print(ans)
