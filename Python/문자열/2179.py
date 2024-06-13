# N = 2*10^4
# 단어 = 100
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(input().strip())
ans = [-1, "", ""]
for i in range(len(arr)-1): # N
    for j in range(i+1, len(arr)): # N
        if ans[0] + 1 >= len(arr[i]):
            break
        if ans[0] + 1 >= len(arr[j]):
            continue
        if arr[i][ans[0]+1] == arr[j][ans[0]+1] and arr[i][:ans[0]+1] == arr[j][:ans[0]+1]:
            idx = ans[0]+2
            while(idx < len(arr[i]) and idx < len(arr[j]) and arr[i][idx] == arr[j][idx]):
                idx += 1
            ans[0] = idx-1
            ans[1] = arr[i]
            ans[2] = arr[j]
print(ans[1])
print(ans[2])
