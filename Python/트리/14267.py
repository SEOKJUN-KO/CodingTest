import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split(" "))
tree = [ [] for _ in range(n+1) ]
sumT = [0]*(n+1)
arr = list(map(int, input().split(" ")))
for i in range(1, n+1):
    if i == 1: continue
    p = arr[i-1]
    tree[p].append(i)
for _ in range(m):
    i, w = map(int, input().split(" "))
    sumT[i] += w

def setScore(p):
    que = deque([p])
    while(que):
        P = que.popleft()
        child = tree[P]
        for c in child:
            sumT[c] += sumT[P]
            que.append(c)
setScore(1)
print(" ".join(map(str,sumT[1:])))
