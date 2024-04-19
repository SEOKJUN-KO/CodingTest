# 야근 피로도 = (남은 작업량)**2의 총합
# 1시간 = 작업량 1
import heapq
def solution(n, works):
    ans = 0
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    for _ in range(n):
        t = -heapq.heappop(heap)
        t -= 1
        if t > 0: heapq.heappush(heap, -t)
        if heap == []: break
    while(heap):
        ans += (-heapq.heappop(heap))**2
    return ans
