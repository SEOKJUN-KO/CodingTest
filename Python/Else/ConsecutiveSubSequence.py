# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    s = set([])
    for i in range(1, len(elements)+1):
        ele = elements+elements[0:i]
        for idx in range(0, len(ele)+1-i ): s.add(sum(ele[idx:idx+i]))
    return len(s)
