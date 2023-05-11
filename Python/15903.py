import heapq
n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapq.heapify(heap)
for _ in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    heapq.heappush(heap, a+b)
print(sum(heap))
