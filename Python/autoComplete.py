# https://school.programmers.co.kr/learn/courses/30/lessons/17685
def calSame(T, C):
    if(T[0] != C[0]): return 1
    i = 1
    while(i < min(len(T), len(C)) and C[:i] == T[:i]):
        i += 1
    if(C[:i] == T[:i]):
        i+=1
    return i

def solution(words):
    answer = 0
    words = sorted(words)
    r = calSame(words[0], words[1])
    answer += len(words[0][:r])
    for i in range(1, len(words)-1):
        r1 = calSame(words[i], words[i-1])
        r2 = calSame(words[i], words[i+1])
        answer += len(words[i][:max(r1, r2)])
    r = calSame(words[-1], words[-2])
    answer += len(words[-1][:r])
    return answer
