import sys, heapq
input = sys.stdin.readline
N = int(input())
dic = {}
longD = 0
for _ in range(N):
    day, value = map(int, input().split())
    if(longD < day): longD = day
    dic[day] = dic.get(day, [])
    dic[day].append(value)

ans = 0
heap = []
for day in range(longD, 0, -1):
    if(day in dic.keys()):
        for value in dic[day]:
            heapq.heappush(heap, -value)
    if(heap):
        ans += heapq.heappop(heap)
print(-ans)
