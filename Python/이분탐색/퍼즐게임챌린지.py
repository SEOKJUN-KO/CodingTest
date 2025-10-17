# diff = 3*10^5
# times = [퍼즐의 소요시간]

def findMinLevel(maxL, diffs, times, limit):
    s, e = 1, maxL
    min_level = e + 1 # 최소 레벨을 저장할 변수

    while(s <= e):
        mid = (s + e) // 2
        
        cnt = 0
        for i in range(len(diffs)):
            if i == 0:
                cnt += times[i]
                continue
            
            if mid >= diffs[i]:
                cnt += times[i]
            else:
                cnt += (times[i] + times[i-1]) * (diffs[i] - mid) + times[i]
            
            # 계산 도중 limit을 넘으면 더 계산할 필요가 없음
            if cnt > limit:
                break
        
        # cnt가 limit을 초과하면 mid가 너무 낮은 것이므로 s를 높여야 함
        if cnt > limit:
            s = mid + 1
        # cnt가 limit 이하면 mid가 정답 후보이므로 e를 낮춰 더 작은 mid를 찾아봄
        else:
            min_level = mid # 현재 mid는 조건을 만족하므로 후보로 저장
            e = mid - 1
            
    return min_level

def solution(diffs, times, limit):
    maxL = max(diffs)    
    return findMinLevel(maxL, diffs, times, limit)