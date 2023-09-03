# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    if len(s)%2 == 1: return 0
    st = []
    for c in s:
        if(st != [] and st[-1] == c): st.pop()
        else: st.append(c)
    if(st == []): return 1
    else: return 0
