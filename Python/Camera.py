https://school.programmers.co.kr/learn/courses/30/lessons/42884?language=python3#

def solution(routes):
    answer = 1
    routes = sorted(routes, key = lambda x: x[0])
    m = routes[0][1]
    for r in routes[1:]:
        if(m >= r[0]):
            if( m > r[1] ): m = r[1]
        else:
            answer += 1
            m = r[1]
    return answer
