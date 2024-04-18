# n개의 집 [10^5]
# 센터 - i 집 = 거리 i
# i 집 - j 집 = 거리 j-i
# cap = 택배 상자 최대 갯수 [50]
# 출력: 최소 이동거리
# 중복 거리를 줄이는 것이 핵심 = 먼 거리부터 움직인다
def solution(cap, n, deliveries, pickups):
    ans = 0
    load, pick = 0, 0
    for i in range(len(deliveries)-1, -1, -1):
        while(load < deliveries[i] or pick < pickups[i]):
            load += cap
            pick += cap
            ans += 2*(i+1)
        load -= deliveries[i]
        pick -= pickups[i]
    return ans
