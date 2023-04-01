import sys, heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    i = int(sys.stdin.readline())
    heapq.heappush(heap, i)
if(len(heap) == 1):
    print(0)
    exit()
ans = 0
while(len(heap) > 1):
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)
    ans += A+B
    heapq.heappush(heap, A+B)
print(ans)
