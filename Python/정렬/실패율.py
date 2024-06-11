# 실패율 = 도달 했으나 클리어 하지 못한 수 / 스테이지에 도달한 플레이어 수
# return 실패율이 높은 스테이지 번호 순 [ 같다면 작은 번호 우선 배치 ]
# N = 500
# stages = 200,000

def solution(N, stages):
    arr = []
    stages = sorted(stages)
    arr = [0]*(max(stages[-1], N)+1)
    for stage in stages:
        arr[stage] += 1
    l = len(stages)
    brr = []
    for i in range(1, N+1):
        if l > 0:
            brr.append([arr[i]/l, i])
        else:
            brr.append([0, i])
        l -= arr[i]
    brr = sorted(brr, key = lambda x: [-x[0], x[1]])
    print(brr)
    ans = [ b[1] for b in brr ]
        
    return ans
