import sys
input = sys.stdin.readline

N, S = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
s = arr[0]
ans = float('inf')

if s >= S: print(1)
else:
    left, right = 0, 0
    while( left <= right and right < N):
        if s < S:
            right += 1;
            if right < N:
                s += arr[right]
                if s >= S and ans > right-left+1: ans = right-left+1
        elif s >= S:
            if left < N:
                s -= arr[left]
                left += 1
                if s >= S and ans > right-left+1: ans = right-left+1
    if ans == float('inf'): print(0)
    else: print(ans)
