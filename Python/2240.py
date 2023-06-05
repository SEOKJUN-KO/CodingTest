import sys

input = sys.stdin.readline
T, H = map( int, input().split() )

ans = 0
j = -1
for i in range(T):
    jadoo = int(input())
    if(jadoo == 2):
        j = i
        break
    ans += 1

pre = 2
cnt = 1
arr = []
if(j != -1):
    for i in range(j+1, T):
        jadoo = int(input())
        if( jadoo != pre ):
            pre = jadoo
            arr.append(cnt)
            cnt = 1
            continue
        cnt +=1
    arr.append(cnt)
    DP = [ [0]*(H+1) for _ in range(len(arr)) ]
    for i in range(H+1):
        if(i%2 == 1):
            DP[0][i] = arr[0]
    for i in range(1, len(arr)):
        for j in range(H+1):
            if(j == 0):
                DP[i][0] = DP[i-1][0]
                if(i%2 == 1):
                    DP[i][0] += arr[i]
            else:
                DP[i][j] = max(DP[i-1][j-1], DP[i-1][j])
                if(i%2 == 1 and j%2 == 0):
                    DP[i][j] += arr[i]
                elif(i%2 == 0 and j%2 == 1):
                    DP[i][j] += arr[i]
    print(max(DP[-1])+ans)
else:
    print(ans)
