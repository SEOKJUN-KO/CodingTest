import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
P = [ i for i in range(V+1)]

heap = []
for _ in range(E):
    u, v, w = map(int, input().split())
    heapq.heappush(heap, [w, u, v])
MST = []

def findP(x):
    if(P[x] == x):
        return x
    return findP(P[x])
def union(x, y):
    X = findP(x)
    Y = findP(y)
    if(X == Y):
        return False
    elif(X < Y):
        P[Y] = X
    else:
        P[X] = Y
    return True
    
while(heap and len(MST) < V-1):
    w, u, v = heapq.heappop(heap)
    R = union(u, v)
    if(R):
        MST.append(w)
print(sum(MST))
