import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split(" ")))
arr = sorted(arr)
M = int(input())
ans = []
for n in map(int, input().split(" ")):
    right = bisect_right(arr, n)
    left = bisect_left(arr, n)
    if right-left > 0: ans.append("1")
    else: ans.append("0")
print(" ".join(ans))