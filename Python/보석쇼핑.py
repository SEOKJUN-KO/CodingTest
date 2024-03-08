def solution(gems):
    answer = [0, 200000]
    s, left, right = {}, 0, 0
    s = set(gems)
    tmp = {}
    while(right < len(gems)):
        if gems[right] not in tmp.keys():
            tmp[gems[right]] = 0
        tmp[gems[right]] += 1
        if len(tmp.keys()) < len(s):
            right += 1
            continue
        if len(tmp.keys()) == len(s):
            while(tmp[gems[left]] > 1):
                tmp[gems[left]] -= 1
                left += 1
            if answer[1]-answer[0] > right-left:
                answer = [left, right]
            right += 1
            
    return [answer[0]+1, answer[1]+1]
