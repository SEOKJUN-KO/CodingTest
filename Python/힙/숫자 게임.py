# N번 비교 / N = 10^5
# 숫자가 클 때만 승점
import heapq

def solution(A, B):
    que = []
    A = sorted(A)
    for i in range(len(B)):
        heapq.heappush(que, B[i])
    i = 0
    while(que):
        o = heapq.heappop(que)
        if A[i] < o: i += 1
    return i
