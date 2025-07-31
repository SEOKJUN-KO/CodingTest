import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
D = [0]
for a in arr:
    D.append(D[-1]+a)
for _ in range(M):
    i, j = map(int, input().split(" "))
    print(D[j]-D[i-1])