import sys
import bisect

input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split(" ")))
for i in range(N): # 10^6
    s = A[i]
    for j in range(i+1, N):
        s += A[j]
        A.append(s)

M = int(input())
B = list(map(int, input().split(" ")))

for i in range(M): # 10^6
    s = B[i]
    for j in range(i+1, M):
        s += B[j]
        B.append(s)
B = sorted(B)

ans = 0
for a in A: # 10^6
    target = T-a
    idxL = bisect.bisect_left(B, target) #20
    idxR = bisect.bisect_right(B, target)#20
    print(idxL, idxR)
    if target != B[idxL] and target != B[idxR]:
        continue
    if target != B[idxL]:
        idxL += 1
    if idxR >= len(B):
        idxR -= 1
    if target != B[idxR]:
        idxR -= 1
    if idxL >= len(B) or idxR < 0:
        continue
    ans += idxR - idxL + 1
    
print(ans)