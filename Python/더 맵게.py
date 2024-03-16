import heapq

def solution(scoville, K):
    ans = 0
    que = []
    for s in scoville:
        heapq.heappush(que, s)
    while(que[0] < K):
        if len(que) == 1: return -1
        a, b = heapq.heappop(que), heapq.heappop(que)
        ans += 1
        heapq.heappush(que, a+(b*2))
    return ans
