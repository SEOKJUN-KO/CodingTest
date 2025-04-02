def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        tmp = ""
        st = bin(( arr1[i] | arr2[i] ))[2:]
        if len(st) < n: tmp += " "*(n-len(st))
        for c in st:
            if c == "1": tmp += "#"
            else: tmp += " "
        ans.append(tmp)
    return ans
