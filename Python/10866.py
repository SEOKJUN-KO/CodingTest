from collections import deque
import sys

deQue = deque()

for _ in range(int(input())):
    I = sys.stdin.readline().strip().split()
    if(len(I) == 2):
        if(I[0] == "push_front"):
            deQue.appendleft(I[1])
        elif(I[0] == "push_back"):
            deQue.append(I[1])
    if(I[0] == "size"):
        print(len(deQue))
    elif(I[0] == "empty"):
        if(deQue):
            print(0)
        else:
            print(1)
    elif(I[0] == "pop_back"):
        if(deQue):
            print(deQue.pop())
        else:
            print(-1)
    elif(I[0] == "pop_front"):
        if(deQue):
            print(deQue.popleft())
        else:
            print(-1)
    elif(I[0] == "front"):
        if(deQue):
            print(deQue[0])
        else:
            print(-1)
    elif(I[0] == "back"):
        if(deQue):
            print(deQue[-1])
        else:
            print(-1)
