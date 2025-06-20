import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = []

pointer = {}
minH = []
maxH = []

for i in range(N):
    arr.append(sorted(list(map(int, input().split(" ")))))
    pointer[arr[i][0]] = [i, 0]
    heapq.heappush(maxH, -arr[i][0])
    heapq.heappush(minH, arr[i][0])

ans = float('inf')

while(True):
    minN = heapq.heappop(minH)
    maxN = -maxH[0]
    ans = min(ans, maxN-minN)
    minArrIdx, idx = pointer[minN]
    del(pointer[minN])
    if idx+1 >= M:
        break
    
    pointer[arr[minArrIdx][idx+1]] = [minArrIdx, idx+1]
    heapq.heappush(minH, arr[minArrIdx][idx+1])
    heapq.heappush(maxH, -arr[minArrIdx][idx+1])

print(ans)