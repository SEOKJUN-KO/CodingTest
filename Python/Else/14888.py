import sys
import itertools
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

op = list(map(int, input().split()))
ops = ['+']*(op[0]) + ['-']*(op[1]) + ['*']*(op[2])+ ['%']*(op[3])

used = [False]*len(ops)
maxA = -float('inf')
minA = float('inf')
def backT(deep, v):
    global maxA, minA
    if (deep == len(used)):
        if(maxA < v):
            maxA = v
        if(minA > v):
            minA = v
        return
    for i in range(len(ops)):
        if(used[i] == False):
            used[i] = True
            if(ops[i] == "+"):
                backT(deep+1, v+arr[deep+1])
            elif(ops[i] == "-"):
                backT(deep+1, v-arr[deep+1])
            elif(ops[i] == "*"):
                backT(deep+1, v*arr[deep+1])
            elif(ops[i] == "%"):
                if(v >= 0):
                    backT(deep+1, v//arr[deep+1])
                else:
                    b = -v
                    b = b//arr[deep+1]
                    backT(deep+1, -b)
            used[i] = False
backT(0, arr[0])
print(maxA)
print(minA)
