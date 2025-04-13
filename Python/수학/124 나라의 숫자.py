def solution(N):
    ans = ''
    n = N
    while(n > 0):
        mok = n//3
        left = n%3
        if (left == 0):
            mok -= 1
            ans += "4"
        else:
            ans += str(left)
        n = mok
        
    return ans[::-1]