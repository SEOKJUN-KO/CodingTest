from heapq import heappush, heappop

def solution(k, tangerine):
    ans = 0
    dic = {}
    for t in tangerine:
        if t not in dic.keys():
            dic[t] = 0
        dic[t] += 1
    heap = []
    for key in dic.keys():
        heappush(heap, -dic[key])
    tmp = 0
    while(True):
        ans += 1
        tmp += -1*heappop(heap)
        if tmp >= k: break
    return ans
