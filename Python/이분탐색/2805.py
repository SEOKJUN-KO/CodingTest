import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
dict = {}
for t in trees:
    if t not in dict.keys(): dict[t] = 0
    dict[t] += 1
treeList = sorted(list(dict.keys()), key=lambda x: x)
low = 0; high = 1000000001
ans = 0
while(low <= high): # log10^9 = 30
    mid = (low+high)//2
    s = 0
    for tree in treeList: # 10^6
        left = tree - mid
        if  left > 0:
            s += left*dict[tree]
    if s >= M and mid > ans: ans = mid
    
    if s >= M: low = mid + 1
    else: high = mid - 1
print(ans)
