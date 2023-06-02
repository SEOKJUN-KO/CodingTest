import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    i = int(input())
    if(i == 0):
        if(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -i)
