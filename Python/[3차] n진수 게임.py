def remain(n):
    if n <= 9: return str(n)
    else:
        if n == 10: return "A"
        if n == 11: return "B"
        if n == 12: return "C"
        if n == 13: return "D"
        if n == 14: return "E"
        if n == 15: return "F"

def makeStr(N, n): #log
    r = ""
    while( N >= n):
        r += remain(N%n)
        N = N//n
        if N < n:
            r += remain(N)
    if r == "":
        r += remain(N%n)
    return r[::-1]
    
def solution(n, t, m, p):
    ans = ''
    i = 0
    tmp, cnt = "", 0
    while(cnt < t):
        r = makeStr(i, n)
        tmp += r
        if len(tmp) >= m:
            ans += tmp[p-1]
            tmp = tmp[m:]
            cnt += 1
        i += 1
    return ans
