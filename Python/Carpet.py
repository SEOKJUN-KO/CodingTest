# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    for i in range(1, yellow+1):
        y = i
        if(yellow%i != 0): continue
        x = yellow // i
        if(2*x+2*y+4 == brown):
            return [x+2, y+2]
            break
