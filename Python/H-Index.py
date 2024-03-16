def solution(citations):
    citations.sort()
    ans = 0
    for i in range(len(citations)):
        if len(citations[i:]) <= citations[i]:
            ans = max(ans, len(citations[i:]))
    return ans
