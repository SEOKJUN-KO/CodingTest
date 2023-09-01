# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    answer = ''
    arr = sorted(list(map(int, s.split())))
    return str(arr[0])+" "+str(arr[-1])
