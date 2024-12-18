import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

board = []

for _ in range(5): board.append(list(input().strip()))

store = []
tmp = []
def backTracking():
    global tmp
    if len(tmp) == 2:
        store.append(copy.deepcopy(tmp))
        return
    for i in range(5):
        tmp.append(i)
        backTracking()
        tmp.pop()
backTracking()

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for arr in combinations(store, 7):
    cnt = 0
    for y, x in arr: 
        if board[y][x] == "S": cnt += 1
    if cnt >= 4:
        que = deque()
        que.append(arr[0])
        s = set([])
        for y, x in arr: s.add(str(y)+" "+str(x))
        s.remove(str(arr[0][0])+" "+str(arr[0][1]))
        while(que):
            y, x = que.popleft()
            for i in range(4):
                Y, X = y+dy[i], x+dx[i]
                if (str(Y)+" "+str(X)) in s:
                    s.remove( str(Y)+" "+str(X) )
                    que.append([Y, X])
        if len(s) == 0: ans += 1
print(ans)
