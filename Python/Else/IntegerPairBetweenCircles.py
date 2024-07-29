# https://school.programmers.co.kr/learn/courses/30/lessons/181187

def solution(r1, r2):
    y1, y2 = r1, r2
    x = 1
    flag1, flag2 = pow(r1, 2), pow(r2, 2)
    answer = 0
    while(x < r1):
        if( flag1 == pow(x,2)+pow(y1, 2) and flag2 >= pow(x,2)+pow(y2, 2)):
            answer += 4*(y2-y1+1)
            x += 1
        elif( flag1 >= pow(x,2)+pow(y1, 2) and flag2 >= pow(x,2)+pow(y2, 2)):
            answer += 4*(y2-y1)
            x += 1
        elif( flag1 < pow(x, 2)+pow(y1, 2) and flag2 < pow(x, 2)+pow(y2, 2)):
            y1 -= 1
            y2 -= 1
        elif( flag1 < pow(x, 2)+pow(y1, 2) ):
            y1 -= 1
        else:
            y2 -= 1
    while(x < r2):
        if( flag2 >= pow(x,2)+pow(y2, 2)):
            answer += y2*4
            x += 1
        else:
            y2 -= 1
    return 4*(r2-r1+1) + answer
