# 계란 1 - 내구도 7, 무게 5
# 계란 2 - 내구도 3, 무게 4
# 계란 1 - 계란 2
# 계란 1: 내구도 - 계란 2 무게 / 계란 2: 내구도 - 계란 1 무게

# 깰 수 있는 계란의 최대 개수
# N = 8

import sys
input = sys.stdin.readline

arr = []
ans = 0
def backT(idx):
    global arr, ans
    if len(arr) == idx:
        cnt = 0
        for a in arr:
            if a[0] <= 0: cnt += 1
        if ans < cnt:
            ans = cnt
        return
    if arr[idx][0] <= 0:
        return backT(idx+1)
    flag = True
    for i in range(len(arr)):
        if i == idx:
            continue
        if arr[i][0] <= 0:
            continue
        arr[idx][0], arr[i][0] = arr[idx][0]-arr[i][1], arr[i][0]-arr[idx][1]
        flag = False
        backT(idx+1)
        arr[idx][0], arr[i][0] = arr[idx][0]+arr[i][1], arr[i][0]+arr[idx][1]
    
    if flag: backT(idx+1)

def solution():
    global arr, ans
    N = int(input())
    for _ in range(N):
        arr.append(list(map(int, input().split(" "))))
    backT(0)
    print(ans)
        
solution()
