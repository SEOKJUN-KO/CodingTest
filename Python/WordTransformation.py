# https://school.programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):
    if target not in words:
        return 0
    arr = []
    def dfs(now):
        if(now == target):
            return len(arr)
        r = 100
        for w in words:
            if(dic[w]): continue
            for i in range(len(now)):
                if( now[:i]+now[i+1:] == w[:i]+w[i+1:] ):
                    dic[w] = True
                    arr.append(w)
                    r = min(r, dfs(w))
                    arr.pop()
                    dic[w] = False
        return r
    dic = {}
    for w in words:
        dic[w] = False
    r = dfs(begin)
    if(r == 100):
        return 0
    else:
        return r
