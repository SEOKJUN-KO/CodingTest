import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

outD = [ set([]) for _ in range(N+1) ]
inD = [0]*(N+1)

for _ in range(M):
    outN, inN = map(int, input().split())
    inD[inN] += 1
    outD[outN].add(inN)
que = deque()
for i in range(1, N+1):
    if( inD[i] == 0):
        que.append(i)
while(que):
    node = que.popleft()
    print(node, end=" ")
    inD[node] = -1
    for n in outD[node]:
        inD[n] -= 1
        if(inD[n] == 0):
            que.append(n)
