import sys
input = sys.stdin.readline

def setMeeting(N):
    arr = []
    for _ in range(N):
        S, E = map(int, input().split(" "))
        arr.append([S, E])
    arr = sorted(arr, key=lambda x: (x[1], -x[0]))
    print(arr)
    return arr

def calculate(arr):
    cnt = 0
    lastE = 0
    for s, e in arr:
        if lastE <= s:
            lastE = e
            cnt += 1
    print(cnt)
    
def solution():
    N = int(input()) # 10^5
    arr = setMeeting(N)
    calculate(arr)
solution()