import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(" "))))
arr = sorted(arr)

ans = 0
heap = []

for s, e in arr:
    while(len(heap) > 0 and heap[0] <= s):
        heapq.heappop(heap)
    heapq.heappush(heap, e)
    ans = max(ans, len(heap))
print(ans)