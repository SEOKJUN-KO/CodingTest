import sys, heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    i = int(sys.stdin.readline())
    if(i == 0 and heap == []):
        print(0)
    elif(i == 0):
        h = heapq.heappop(heap)
        print(h[1])
    else:
        if(i>0):
            heapq.heappush(heap, (i+0.1, i))
        else:
            heapq.heappush(heap, (abs(i), i))
