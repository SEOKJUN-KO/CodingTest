from collections import deque
def solution(queue1, queue2):
    s1, s2 = 0, 0
    for q in queue1:
        s1 += q
    for q in queue2:
        s2 += q
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    while(s1 != s2):
        if s1 > s2:
            t = queue1.popleft()
            queue2.append(t)
            s1 -= t
            s2 += t
        else:
            t = queue2.popleft()
            queue1.append(t)
            s2 -= t
            s1 += t
        cnt += 1
        if cnt == 900000: break
    if cnt == 900000: return -1
    return cnt
