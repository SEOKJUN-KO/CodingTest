from collections import deque
from heapq import heappush, heappop
# N = 5*10^6
# L = 5*10^6


def findRange(L, i): # 1
    return [max(0, i-L+1), i]


def caculate(A, L):
    ans = []
    l, r = 0, 0
    heap = []
    popHeap = []
    for i in range(len(A)): # 5*10^6
        s, e = findRange(L, i)
        while(r <= e):
            R = A[r]
            heappush(heap, R)
            r += 1
        while(l < s):
            lN = A[l]
            heappush(popHeap, lN)
            l += 1
        while( len(popHeap) > 0 and popHeap[0] == heap[0] ): # logL
            heappop(popHeap)
            heappop(heap)
        ans.append(heap[0])
    return ans

def main(): 
    _, L = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))
    arr = caculate(A, L)
    print(" ".join(map(str, arr)))
main()
