import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split() ))
    arr = arr[::-1]
    m = arr[0]
    i = 0
    ans = 0
    while(i < len(arr)):
        if(m < arr[i]):
            for a in arr[:i]:
                ans += m - a
            arr = arr[i:]
            m = arr[0]
            i = 0
        i += 1
    for a in arr:
        ans += m - a
    print(ans)
