import sys, heapq
n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, -int(input()))
    
ans = 0
i = 1
while(heap):
    A = heapq.heappop(heap)
    if(ans < -A*i):
        ans = -A*i
    i += 1
print(ans)
