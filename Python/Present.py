# https://www.codetree.ai/training-field/search/problems/the-grace-form-teacher/description?page=1&pageSize=20&tier=8%2C8
import sys
input = sys.stdin.readline

N, B = map(int, input().split() )
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key = lambda x: (x[0]//2+x[1]))
ans = 0
for i in range(len(arr)-1, -1, -1):
    s = arr[i][0]//2 + arr[i][1]
    if(s > B):
        continue
    tmp = 1
    for j in range(0, i):
        if(s > B):
            if( ans < tmp-1 ):
                ans = tmp-1
            break
        s += arr[j][0] + arr[j][1]
        tmp += 1
    if(s > B):
        if( ans < tmp-1 ):
            ans = tmp-1
    else:
        if( ans < tmp ):
            ans = tmp
print(ans)
