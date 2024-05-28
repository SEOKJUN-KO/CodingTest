import sys
from collections import deque

input = sys.stdin.readline

def calculate(W, H):
    ans = 0
    for i in range(1, W):
        DP[0][i] = DP[0][0]
    for h in range(1, H):
        DP[h][0] = DP[h-1][0]
        for w in range(1, W):
            DP[h][w] += DP[h][w-1] + DP[h-1][w]
    return DP[-1][-1]

N, M, K = map(int, input().split())

h, w = 1, 1
while(M*h < K):
    h += 1
w = K - M*(h-1)
nh, nw = N-h+1, M*h-K+1

DP = [ [0]*w for _ in range(h) ]
DP[0][0] = 1
a = calculate(w, h)
if(K == 0):
    print(a)
    exit()
DP = [ [0]*nw for _ in range(nh) ]
DP[0][0] = a
b = calculate(nw, nh)
print(b)
