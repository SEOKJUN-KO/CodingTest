import sys; input = sys.stdin.readline
from heapq import heappush, heappop

N, M, K = map(int, input().split(" "))
parent = [ i for i in range(N+1) ]
heap = []

power = set(list( map(int, input().split(" ")) ))

for _ in range(M):
    u, v, w = map(int, input().split(" "))
    heappush(heap, [w, u, v])
    
def find(x):
    if x == parent[x]: return parent[x]
    return find(parent[x])

def union(x, y):
    X = find(x)
    Y = find(y)
    if X == Y: return False
    if X in power and Y in power: return False

    if X < Y:
        if Y in power:
            power.remove(Y)
            power.add(X)
        parent[Y] = X
    else:
        if X in power:
            power.remove(X)
            power.add(Y)
        parent[X] = Y
    return True
    
ans = 0
while(heap):
    w, u, v = heappop(heap)
    if union(u, v): ans += w
print(ans)
