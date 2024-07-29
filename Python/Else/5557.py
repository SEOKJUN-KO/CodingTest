N = int(input())
nums = list(map(int, input().split()))

dic = {nums[0]: 1}
for i in range(1, N-1):
    tmp = dic.copy()
    for k in dic.keys():
        if( k + nums[i] <= 20):
            tmp[k+nums[i]] = tmp.get(k+nums[i], 0) + dic[k]
        if( k - nums[i] >= 0):
            tmp[k-nums[i]] = tmp.get(k-nums[i], 0) + dic[k]
        tmp[k] -= dic[k]
        if(tmp[k] == 0):
            del(tmp[k])
    dic = tmp.copy()
ans = dic.get(nums[-1], 0)
print(ans)
