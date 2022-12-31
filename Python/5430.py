import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    que = deque(arr)

    rev = 0
    flag = 0
    if n == 0:
        que = []

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(que) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    que.popleft()
                else:
                    que.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(que) + "]")
        else:
            que.reverse()
            print("[" + ",".join(que) + "]")
