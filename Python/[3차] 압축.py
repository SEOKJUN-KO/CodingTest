def solution(msg):
    ans = []
    dic, st, lastN = {}, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 27
    for i in range(len(st)):
        dic[st[i]] = i+1
    st = ""
    for m in msg:
        if st+m in dic.keys():
            st += m
            continue
        ans.append(dic[st])
        dic[st+m] = lastN
        lastN += 1
        st = m
    if st != "" and st in dic.keys(): ans.append(dic[st])
    else: ans.append(lastN)
    return ans
