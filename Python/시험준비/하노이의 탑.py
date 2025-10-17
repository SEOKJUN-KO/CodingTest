answer = []

def move(number, now, mid, target):
    if number == 1:
        answer.append([now, target])
        return
    move(number-1, now, target, mid) #위에꺼 치우기
    answer.append([now, target])# 본인 움직임
    move(number-1, mid, now, target)# 위에꺼 다시 불러오기
    
def solution(n):
    global answer
    move(n, 1, 2, 3)
    return answer