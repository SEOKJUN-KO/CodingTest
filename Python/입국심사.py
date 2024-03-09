def solution(n, times):
    times = times
    times.sort()
    left, right = 1, 9999999999999
    answer = right
    while(left <= right):
        mid = (left+right)//2
        tmp = 0
        for t in times:
            tmp += mid//t
            if tmp > n: break
        if tmp >= n:
            if answer > mid:
                answer = mid
            right = mid - 1
        elif tmp < n:
            left = mid + 1
    return answer
