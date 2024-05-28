import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
A = [ [float('inf')]*(n+1) for _ in range(n+1) ]
Nxt = [ [0]*(n+1) for _ in range(n+1) ]
for _ in range(m):
    s, e, w = map( int, input().split() )
    if(w < A[s][e]):
        A[s][e] = w
        Nxt[s][e] = e
for i in range(1, n+1):
    A[i][i] = 0
    
for i in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if(A[start][i]+A[i][end] < A[start][end]):
                A[start][end] = A[start][i]+A[i][end]
                Nxt[start][end] = Nxt[start][i]
for a in A[1:]:
    for i in range(1, len(a)):
        if(a[i] != float('inf')):
            print(a[i], end=" ")
            continue
        print(0, end=" ")
    print()
 

def findPath(s, e):
    if(Nxt[s][e] == 0):
        return []
    now = s
    arr = [s]
    while(now != e):
        now = Nxt[now][e]
        arr.append(now)
    return arr

for i in range(1, n+1):
    for j in range(1, n+1):
        out = findPath(i, j)
        print(len(out), end =" ")
        print(" ".join(map(str,out)))
