# 투 포인터
import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))

arr = []
for i in range(N):
    for n in map(int, input().split(" ")):
        arr.append([i, n])

arr = sorted(arr, key=lambda x: x[1])


save = [ 0 for _ in range(N)] # 10^3
cnt = 0
leftP, rightP = 0, 0
limit = N*M
ans = float('inf')
while(True):
    while(True):
        now, n = arr[rightP]
        if save[now] == 0: cnt += 1
        save[now] += 1
        rightP += 1
        if rightP == limit or cnt == N: break 
        
    while(True):
        now, n = arr[leftP]
        if save[now] == 1: break
        save[now] -= 1
        if save[now] == 0: cnt -= 1
        leftP += 1
        if leftP == limit or rightP-1 == leftP: break
    if ans > arr[rightP-1][1] - arr[leftP][1]:
        ans = arr[rightP-1][1] - arr[leftP][1]
    if rightP == limit: break
print(ans)

# --------------------------------------------------------------------------------------------------------------------------------------------

# 힙 사용
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