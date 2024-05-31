# N = 2000

def solution(cookie):
    ans = 0
    arr = [0]
    brr = [0]
    for c in cookie:
        arr.append(arr[-1]+c)
    for c in cookie[::-1]:
        brr.append(brr[-1]+c)
    arr.append(0)
    brr.append(0)
    brr = brr[::-1]
    for m in range(1, len(arr)-1):
        l, r = 0, len(brr)-1
        while(l < m and m < r):
            if arr[m]-arr[l] > brr[m+1]-brr[r]:
                l += 1
            elif arr[m]-arr[l] < brr[m+1]-brr[r]:
                r -= 1
            elif arr[m]-arr[l] == brr[m+1]-brr[r]:
                ans = max(ans, arr[m]-arr[l])
                break
    return ans
