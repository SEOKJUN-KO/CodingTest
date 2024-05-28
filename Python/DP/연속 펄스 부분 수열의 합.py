# n = 10^6 -> 모두 다른 숫자
# 단 한개가 남을 때까지
# 임의의 인접한 두 풍선 선택 후 하나 터트리기 터진 -> 풍선으로 인해 빈공간 생성 -> 밀착
#      (숫자 큰 풍선 터트리기 일반적, 단 1회 작은 풍선 가능)
# 최후로 남기는 것이 가능한 풍선들의 개수 반환
# 각각 풍선 하나씩 비교 = 10^6
# -------------
# 기준 풍선보다 작은 것 터트리면서 하나만 남기기
# 큰 풍선은 상관 없음
# -------------

def solution(a):
    ans = 2
    S = a.copy()
    E = a.copy()
    for i in range(1, len(S)):
        if S[i-1] < S[i]: S[i] = S[i-1]
    for i in range(len(S)-1, 0, -1):
        if E[i-1] > E[i]: E[i-1] = E[i]
    for i in range(1, len(a)-1):
        if S[i-1] > a[i] or E[i+1] > a[i]: ans += 1
    return ans
