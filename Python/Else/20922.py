N, M = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
dic = {arr[0]: 1}
ans = 0
while(left < N and right < N and left <= right):
    if(dic[arr[right]] > M):
        dic[arr[left]] -= 1
        left += 1
    else:
        if(ans < right-left+1): ans = right-left+1
        right += 1
        if(right == N):
            break
        dic[arr[right]] = dic.get(arr[right], 0) + 1
print(ans)
