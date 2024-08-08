from collections import deque
import sys

input = sys.stdin.readline
n, w, L = map(int, input().split(" "))
truck = list(map(int, input().split(" ")))
que = deque()
total = 0
idx = 0
time = 0

while( idx < len(truck) ):
    if len(que) == w:
        total -= que.popleft()
    if total + truck[idx] <= L:
        que.append(truck[idx])
        total += truck[idx]
        idx += 1
    else:
        que.append(0)
    time += 1
print(time+w)
