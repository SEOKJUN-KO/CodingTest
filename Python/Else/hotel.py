# https://school.programmers.co.kr/learn/courses/30/lessons/155651#
import heapq
def solution(book_time):
    book_time = sorted(book_time, key=lambda x: x[0])
    info = book_time[0][1].split(":")
    ans = 1
    heap = []
    heapq.heappush(heap, int(info[0])*60+int(info[1])+10)
    for b in book_time[1:]:
        infoS = b[0].split(":")
        sT = int(infoS[0])*60+int(infoS[1])
        infoE = b[1].split(":")
        eT = int(infoE[0])*60+int(infoE[1])+10
        if( heap[0] > sT ):
            heapq.heappush(heap, eT)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, eT)
        ans = max(ans, len(heap))
    return ans
