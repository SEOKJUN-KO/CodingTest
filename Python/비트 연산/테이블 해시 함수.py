def solution(data, col, row_begin, row_end):
    ans = 0
    D = sorted(data, key=lambda x: (x[col-1], -x[0]) )
    
    for i in range(row_begin, row_end+1):
        s = 0
        for j in D[i-1]:
            s += j%i
        ans ^= s
        
    return ans