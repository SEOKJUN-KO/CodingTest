def solution(n):
    if(n == 1): return 1
    ans = 1
    while(n > 1):
        if n % 2 == 0:
            n = n//2
        else:
            n -= 1
            ans += 1
    return ans
