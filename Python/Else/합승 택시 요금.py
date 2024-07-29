# S -> A | S -> B | S -> 특정 지점까지[S를 제외한 모든 노드] 간 다음 -> A / B
# 일단 각자 최단 경로를 계산한다.
# n = 2*10^2
# n*n*logn = 4*10^5
import heapq

board = []
def getMINARR(start, n):
    global board
    minArr = [float('inf')]*(n+1)
    heap = []
    heap, minArr[start] = [[0, start]], 0
    while(heap):
        w, node = heapq.heappop(heap)
        if minArr[node] != w: continue
        for edge, end in board[node]:
            if minArr[end] > edge+w:
                minArr[end] = edge+w
                heapq.heappush(heap, [minArr[end], end])
    return minArr
def solution(n, s, a, b, fares):
    minArr = [float('inf')]*(n+1)
    heap, minArr[s] = [[0, s]], 0
    global board
    board = [[] for _ in range(n+1) ]
    for f in fares:
        s, e, w = f
        board[s].append([w, e])
        board[e].append([w, s])
    while(heap):
        w, node = heapq.heappop(heap)
        if minArr[node] != w: continue
        for edge, end in board[node]:
            if minArr[end] > edge+w:
                minArr[end] = edge+w
                heapq.heappush(heap, [minArr[end], end])
    answer = minArr[a]+minArr[b]
    for i in range(1, n+1):
        if minArr[i] == float('inf'): continue
        tmp = minArr[i]
        re = getMINARR(i, n)
        tmp += re[a]+re[b]
        if answer > tmp: answer = tmp
    return answer
