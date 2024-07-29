# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    leng = len(computers)
    for k in range(leng):
        for i in range(leng):
            for j in range(leng):
                if(computers[i][j] == 0 and computers[i][k] == 1 and computers[k][j] == 1):
                    computers[i][j] = 1
    answer = 0
    connect = [False]*(leng)
    for i in range(leng):
        if(connect[i] == False):
            answer += 1
            for j in range(leng):
                if( computers[i][j] == 1 ): connect[j] = True
    return answer
