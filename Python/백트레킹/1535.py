import sys

N = int(input())
arr = list(map(int, input().split())) # 잃는 체력
brr = list(map(int, input().split())) # 얻는 기쁨
maxH = 0
def backT(deep, life, happy):
    global maxH, N
    if(deep == N-1):
        if(maxH < happy and life > 0):
            maxH = happy
        return
    backT(deep+1, life-arr[deep+1], happy+brr[deep+1])
    backT(deep+1, life, happy)
backT(0, 100-arr[0], 0+brr[0])
backT(0, 100, 0)
print(maxH)
