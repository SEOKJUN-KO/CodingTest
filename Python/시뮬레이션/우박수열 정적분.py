def solution(k, ranges):
    ans = []
    arr = [k]
    size = []
    while(arr[-1] != 1):
        if arr[-1]%2 == 0:
            arr.append(arr[-1]//2)
        else:
            arr.append(arr[-1]*3+1)
        if (len(arr)>1):
            mx, mn = max(arr[-1], arr[-2]), min(arr[-1], arr[-2])
            size.append((mx-mn)/2 +mn)
    for a, b in ranges:
        start, end = a, len(arr)-1+b
        if (start > end): 
            ans.append(-1)
            continue
        cnt = 0
        for i in range(start, end):
            cnt += size[i]
        ans.append(cnt)
    
    return ans