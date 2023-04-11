import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
A = [ [float('inf')]*(n+1) for _ in range(n+1) ]
for _ in range(m):
    s, e, w = map(int, input().split())
    A[s][e] = min(w, A[s][e])
for i in range(1, n+1):
    A[i][i] = 0
    
for i in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if(A[start][i]+A[i][end] < A[start][end]):
                A[start][end] = A[start][i]+A[i][end]
for a in A[1:]:
    for i in range(1, len(a)):
        if(a[i] != float('inf')):
            print(a[i], end=" ")
            continue
        print(0, end=" ")
    print()
