# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    tmp = words[0]
    s = set([words[0]])
    for i in range(1, len(words)):
        if(tmp[-1] != words[i][0] or words[i] in s): return [i%n+1, i//n+1]
        s.add(words[i])
        tmp = words[i]
    return [0, 0]
