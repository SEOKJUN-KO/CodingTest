import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
state = [False]*(V+1)
boards = [ [] for _ in range(V+1) ]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    boards[a].append(b)
    boards[b].append(a)

que = deque()
state[1] = True
que.append([1, 0])
def spread():
    global V
    ans = 0
    while(que):
        v, deep = que.popleft()
        for i in boards[v]:
            if( state[i] == False and deep <= 1):
                state[i] = True
                que.append([i, deep+1])
                ans += 1
    return ans
print(spread())
