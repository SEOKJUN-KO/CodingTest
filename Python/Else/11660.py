import sys
N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(1, N):
    arr[0][i] += arr[0][i-1]

for y in range(1, N):
    for x in range(1, N):
        arr[y][x] += arr[y][x-1]
    for x in range(1, N):
        arr[y][x] += arr[y-1][x]
    arr[y][0] += arr[y-1][0]

for _ in range(M):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    ans = arr[r2-1][c2-1]
    if( r1 == 1 and c1 == 1):
        ans += 0
    elif( r1 == 1):
        ans -= arr[r2-1][c1-2]
    elif( c1 == 1):
        ans -= arr[r1-2][c2-1]
    else:
        ans -= arr[r1-2][c2-1] + arr[r2-1][c1-2]
        ans += arr[r1-2][c1-2]
    print(ans)
