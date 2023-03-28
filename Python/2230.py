import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A = sorted(A)

ans = float('inf')
start, end = 0, 0
while(start<N and end<N):
    if(A[end]-A[start] < M):
        end += 1
    elif(A[end]-A[start] == M):
        print(M)
        exit()
    elif(A[end]-A[start] > M):
        ans = min(ans, A[end]-A[start])
        start += 1
        
print(ans)
