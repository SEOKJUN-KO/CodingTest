def solution(enroll, referral, seller, amount):
    ans = []
    dic = {}
    sumDic = {}
    for i in range(len(enroll)):
        sumDic[enroll[i]] = 0
        if referral[i] == "-":
            dic[enroll[i]] = "center"
        else:
            dic[enroll[i]] = referral[i]
    for i in range(len(seller)):
        q, w = seller[i], amount[i]*100
        while(q != "center" and w >= 10):
            sumDic[q] += w - w//10
            q = dic[q]
            w = w//10
        if q!= "center":
            sumDic[q] += w
    for i in range(len(enroll)):
        ans.append(sumDic[enroll[i]])
    return ans
