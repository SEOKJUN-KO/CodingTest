# n = 10^7
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        y = i//n
        x = i%n
        if x <= y: answer.append(y+1)
        else: answer.append(x+1)
    return answer

# 1 2 3 4 5 6
# 2 2 3 4 5 6
# 3 3 3 4 5 6
# 4 4 4 4 5 6
# 5 5 5 5 5 6
# 6 6 6 6 6 6
############
# x <= y -> y
# x > y -> x
##############
# n = 행마다 n개의 값 존재
# left
# y = left//n x = left%n
