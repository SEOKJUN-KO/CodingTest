def solution(n, s):
    if (n > s): return [-1]
    if (s%n) == 0: return [s//n]*n
    ans = [s//n for _ in range(n)]
    for i in range(s%n):
        idx = i%len(ans)
        ans[idx] += 1
    
    return ans[::-1]