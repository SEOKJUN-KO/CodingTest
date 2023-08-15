# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    answer = []
    stack = []
    plans = sorted(plans, key = lambda x: x[1])
    stack.append([int(plans[0][2]), plans[0][0]])
    for i in range(1, len(plans)):
        r = calTime(plans[i-1][1], plans[i][1])
        while(stack != [] and r >= stack[-1][0]):
            r -= stack[-1][0]
            p = stack.pop()
            answer.append(p[1])
        if(r > 0 and stack != []):
            stack[-1][0] = stack[-1][0] - r
        stack.append([int(plans[i][2]), plans[i][0]])
    while(stack):
        p = stack.pop()
        answer.append(p[1])
    return answer

def calTime(start, nxtStart):
    nH, nM = map(int, nxtStart.split(":"))
    H, M = map(int, start.split(":"))
    return (nH-H)*60+nM-M
