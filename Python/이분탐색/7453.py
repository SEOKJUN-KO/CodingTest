import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def getFourArray(N):
    arr = [[], [], [], []]
    for _ in range(N): # 4*10^3
        tmp = list(map(int, input().split(" ")))
        for i in range(4):
            arr[i].append(tmp[i])
    return arr

def makeSumArray(arr):
    CD = []
    # 0.X초
    for c in arr[2]:
        for d in arr[3]:
            CD.append(c+d)

    CD = sorted(CD, key=lambda x: x) #3초
    return CD

def calculate(arr, CD):
    ans = 0
    for a in arr[0]:
        for b in arr[1]: 
            l = bisect_left(CD, -(a+b))
            r = bisect_right(CD, -(a+b))
            ans += r-l
    
    return ans

def main():
    N = int(input())
    arr = getFourArray(N)
    CD = makeSumArray(arr)
    print(calculate(arr, CD))
main()