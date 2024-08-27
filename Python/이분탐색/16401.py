import sys
input = sys.stdin.readline

M, N = map(int, input().split(" "))
snacks = list(map(int, input().split(" ")))
snackD = {}
for l in snacks: # 10^6
    if l not in snackD.keys(): snackD[l] = 1; continue
    snackD[l] += 1
snacks = list(set(snacks))
snacks.sort()

def findIndex(L):
    global snacks
    left, right = 0, len(snacks)
    while(left < right):
        mid = (left+right)//2
        if snacks[mid] == L: return mid
        if snacks[mid] > L: right = mid
        else: left = mid+1
    return mid

left, right = snacks[0], snacks[-1]+2
ans = 0
while(left <= right):
    mid = (left+right)//2
    print(mid)
    startIdx = findIndex(mid)
    cnt = 0
    for i in range(max(0, startIdx-1), len(snacks)):
        if snacks[i] < mid: continue
        cnt += (snacks[i]//mid)*snackD[snacks[i]]
    if cnt >= M:
        if ans < mid: ans = mid
        left = mid + 1
    else: right = mid - 1
print(ans)
