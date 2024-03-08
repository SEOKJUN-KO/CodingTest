import heapq

def find(p, x):
    if p[x] == x:
        return x
    return find(p, p[x])

def union(p, x, y):
    px = find(p, x)
    py = find(p, y)
    if px < py:
        p[py] = px
    else :
        p[px] = py

def solution(n, costs):
    parents = [ i for i in range(0, n+1) ]
    answer = 0
    heap = []
    for c in costs:
        n1, n2, w = c[0], c[1], c[2]
        heapq.heappush(heap, [w, n1, n2])
    while(heap):
        w, n1, n2 = heapq.heappop(heap)
        pn1 = find(parents,n1)
        pn2 = find(parents,n2)
        if pn1 == pn2:
            continue
        answer += w
        union(parents, n1, n2)
    return answer
