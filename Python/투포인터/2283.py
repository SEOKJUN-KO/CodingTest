import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N, K = map(int, input().split(" "))

dic = {}
for _ in range(N): 
    s, e = map(int, input().split(" "))
    if s not in dic.keys(): dic[s] = 0
    if e not in dic.keys(): dic[e] = 0
    dic[s] += 1; dic[e] -= 1

keyL = sorted(list(dic.keys()))

def main():
    global dic, K
    A, B = 0, 0
    aL, bL = 0, 0
    k = 0
    if 0 in dic.keys(): aL, bL = dic[0], dic[0]
    while(A <= B and B <= 1000000):
        if k == K:
            print(A, B)
            return
        elif k > K:
            k -= aL
            A += 1
            if A in dic.keys(): aL += dic[A]
        elif k < K:
            k += bL
            B += 1
            if B in dic.keys(): bL += dic[B]
    print(0, 0)
    return
main()
