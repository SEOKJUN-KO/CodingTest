import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
    
arr = sorted(arr)
cnt, maxcnt, val, maxval = 0, 0, arr[0], arr[0]
for i in range(len(arr)):
    if(arr[i] == val):
        cnt += 1
        if(i == len(arr)-1 and cnt > maxcnt):
            maxval = val
    else:
        if(cnt > maxcnt):
            maxcnt = cnt
            maxval = val
        val = arr[i]
        cnt = 1
print(maxval)
