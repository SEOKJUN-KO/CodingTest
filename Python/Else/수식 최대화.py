# 연산자 우선순위
from collections import deque

order = [
    ["+", "-", "*"],
    ["+", "*", "-"],
    ["-", "+", "*"],
    ["-", "*", "+"],
    ["*", "+", "-"],
    ["*", "-", "+"]]

def solution(expression):
    answer = 0
    numArr = deque()
    operArr = deque()
    tmp = ""
    for e in expression:
        if e == "+" or e == "-" or e == "*":
            numArr.append(int(tmp))
            operArr.append(e)
            tmp = ""
        else:
            tmp += e
    numArr.append(int(tmp))
    # print(numArr, operArr)
    for orde in order:
        numQue = numArr.copy()
        operQue = operArr.copy()
        for o in orde:
            tmpN = deque()
            tmpO = deque()
            while(len(numQue) > 1):
                one = numQue.popleft()
                two = numQue.popleft()
                oper = operQue.popleft()
                if oper == o:
                    if o == "+":
                        numQue.appendleft(one+two)
                    elif o == "-":
                        numQue.appendleft(one-two)
                    elif o == "*":
                        numQue.appendleft(one*two)
                else:
                    tmpN.append(one)
                    numQue.appendleft(two)
                    tmpO.append(oper)
            tmpN.append(numQue.popleft())
            numQue = tmpN
            operQue = tmpO
        if(len(numQue) == 1):
            n = numQue.popleft()
            if answer < abs(n):
                answer = abs(n)
        
    return answer
