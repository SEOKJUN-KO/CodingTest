import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    k = 2
    arr = []
    while(True):
        if( k > a or k > b ):
            arr.append(a)
            arr.append(b)
            break
        if( a%k == 0 and b%k == 0 ):
            arr.append(k)
            a = a//k
            b = b//k
        else:
            k += 1
    ans = 1
    for a in arr:
        ans *= a
    print(ans)
