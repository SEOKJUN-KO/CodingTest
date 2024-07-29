from collections import deque
def solution(progresses, speeds):
    answer = []
    que = deque()
    for i in range(len(progresses)):
        que.append([progresses[i], speeds[i]])
    days = 0
    days += (100-progresses[0]-speeds[0]*days )//speeds[0]
    if (100-progresses[0])%speeds[0] > 0: days += 1
    tmp = 0
    while(que):
        progress, speed = que.popleft()
        if 100-progress-speed*days <= 0:
            tmp += 1
        else:
            answer.append(tmp)
            tmp = 1
            days += (100-progress-speed*days )//speed
            if (100-progress)%speed > 0: days += 1
    answer.append(tmp)
    return answer
