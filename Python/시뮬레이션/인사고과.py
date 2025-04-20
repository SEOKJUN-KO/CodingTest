# 근태, 동료 평가 둘 다 낮은 경우 석차 제외
# 점수 합 석차 차등 지급
# n = 10^5
# 완호의 등수를 반환
# 같은 점수에서는, 어떤 사원 보다 두 점수가 모든 낮은 경우가 없다.
# 더 높은 점수와 모두를(?) 비교하여, 낮은 점수가 둘다 낮은 경우는 있다.

def solution(scores):
    w = scores[0]
    arr = sorted(scores, key=lambda x: ( -(x[0]+x[1]) ) ) # nlogn
    dic = {}
    totalCnt = 0
    for a, b in arr: # n
        flag = True
        if a > w[0] and b > w[1]:
            return -1
        
        for key in dic.keys(): # 9
            if key <= a: continue
            if (dic[key] >> (b)) > 0:
                flag = False
                break
        
        if w == [a, b]:
            break
        
        if flag:
            totalCnt += 1
                
        if a not in dic.keys():
            dic[a] = 0
        dic[a] |= (1 << (b-1))    
    
    return totalCnt+1