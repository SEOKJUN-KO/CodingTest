# 점선 - 오르막 실선 - 내리막
# 최악 - 최선 = 출력
import sys
input = sys.stdin.readline
N, M = map(int, input().split(" "))
p = [i for i in range(N+1)]
arr = []

def find(x):
    if x == p[x]: return x
    return find(p[x])
def union(x, y):
    X = find(x)
    Y = find(y)
    if X < Y:
        p[Y] = X
    else:
        p[X] = Y
    
ansA, ansB, cntA, cntB = 0, 0, 1, 1
tmp = list(map(int, input().split(" ")))
if tmp[2] == 0:
    ansA += 1
    ansB += 1
p[1] = 0
for _ in range(M):
    tmp = list(map(int, input().split(" ")))
    arr.append(tmp[::-1])
arr = sorted(arr, key=lambda x: -x[0])

for w, x, y in arr:
    if cntA == N: break
    if find(x) == find(y): continue
    union(x, y)
    if w == 0: ansA += 1
    cntA += 1

p = [i for i in range(N+1)]
p[1] = 0
for w, x, y in arr[::-1]:
    if cntB == N: break
    if find(x) == find(y): continue
    union(x, y)
    if w == 0: ansB += 1
    cntB += 1

print(ansB**2 - ansA**2)
