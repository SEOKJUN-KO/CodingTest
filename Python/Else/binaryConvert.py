def solution(s):
    ans = [0, 0]
    while(s != "1"):
        c = s.count("0")
        ans[1] += c
        s = bin(len(s)-c)[2:]
        ans[0] += 1
    return ans
