import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    _, s, e = map(int, input().split(" "))
    arr.append([s, e])
arr = sorted(arr)
heap = []
ans = 1
for s, e in arr:
    if heap == []:
        heapq.heappush(heap, e)
        continue
    if heap[0] > s:
        heapq.heappush(heap, e)
        ans = max(ans, len(heap))
    else:
        while(heap != [] and heap[0] <= s):
            heapq.heappop(heap)
        heapq.heappush(heap, e)
print(ans)
