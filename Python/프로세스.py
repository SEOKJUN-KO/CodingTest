# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
from collections import deque

def solution(priorities, location):
    
    dic = {}
    que = deque()
    arr = []
    for i in range(len(priorities)):
        que.append([i, priorities[i]])
        arr.append(priorities[i])
    arr.sort(key=lambda x: x)
    ans = 0
    while(que):
        idx, p = que.popleft()
        if arr[-1] == p:
            ans += 1
            if idx == location:
                return ans
            arr.pop()
            continue
        que.append([idx, p])
