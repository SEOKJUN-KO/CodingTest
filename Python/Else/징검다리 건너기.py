# stone = 2*10^5
# life = 2*10^8
# => 54*10^5
def solution(stones, k):
    answer, dic = float('inf'), {}
    s = list(set(stones))
    s.sort()
    left, right = s[0], s[-1]
    while(left <= right):
        mid = (left+right)//2
        tmpc = 0
        for i in range(len(stones)):
            if stones[i] <= mid:
                tmpc += 1
                if tmpc == k:
                    if answer > mid:
                        answer = mid
                    break
            else:
                tmpc = 0
        if tmpc < k:
            left = mid+1
        else:
            right = mid-1
    return answer
