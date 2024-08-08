import sys
from collections import deque
input = sys.stdin.readline
arr = []
for _ in range(4):
    arr.append(deque(map(int, input().strip())))
k = int(input())

def rotate(i, d, flow):
    for j in [i-1, i+1]:
        if 0 <= j < 4:
            if ((flow == 0 or flow == -1) and j == i-1 and (arr[i][6] != arr[j][2])):
                rotate(j, -d, -1)
            elif ((flow == 0 or flow == 1) and j == i+1 and (arr[i][2] != arr[j][6])):
                rotate(j, -d, 1)
    if d == 1:
        tmp = arr[i].pop()
        arr[i].appendleft(tmp)
    else:
        tmp = arr[i].popleft()
        arr[i].append(tmp)

for _ in range(k):
    i, d = map(int, input().split(" "))
    rotate(i-1, d, 0)

tmp = 1
ans = 0
for i in range(4):
    ans += arr[i][0]*tmp
    tmp = tmp*2

print(ans)
