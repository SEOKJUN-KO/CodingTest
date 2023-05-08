import sys

input = sys.stdin.readline

n = int(input())
cnt = 1
while(n != 0):
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr[1][0] += arr[0][1]
    arr[1][1] += min(arr[0][1], arr[0][1]+arr[0][2], arr[1][0])
    arr[1][2] += min(arr[0][1], arr[0][1]+arr[0][2], arr[1][1])
    
    for h in range(2, len(arr)):
        arr[h][0] += min(arr[h-1][0], arr[h-1][1])
        arr[h][1] += min(arr[h-1][0], arr[h-1][1], arr[h-1][2], arr[h][0])
        arr[h][2] += min(arr[h-1][1], arr[h-1][2], arr[h][1])
        
    print(cnt, end="")
    print(".",arr[-1][1])
    n = int(input())
    cnt += 1
