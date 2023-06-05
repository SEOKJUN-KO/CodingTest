import sys, heapq

input = sys.stdin.readline
N = int(input())

heap = []
for _ in range(N):
    arr = list(map(int, input().split()))
    for a in arr:
        if(len(heap) < N):
            heapq.heappush(heap, a)
        elif( heap[0] < a ):
            heapq.heapreplace(heap, a)
print(heap[0])
