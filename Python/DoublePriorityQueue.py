# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq
def solution(operations):
    minH = []
    maxH = []
    dic = {}
    for o in operations:
        mode, i = o.split(" ")
        i = int(i)
        if(mode == "I"):
            heapq.heappush(minH, i)
            heapq.heappush(maxH, -i)
            dic[i] = dic.get(i, 0) + 1
        else:
            if( i == 1 and maxH != [] ):
                while(maxH):
                    tmp = -heapq.heappop(maxH)
                    if( dic[tmp] <= 0 ):
                        continue
                    dic[tmp] -= 1
                    break
            elif( i == -1 and minH != []):
                while(minH):
                    tmp = heapq.heappop(minH)
                    if( dic[tmp] <= 0 ):
                        continue
                    dic[tmp] -= 1
                    break
    answer = [0, 0]
    while(maxH):
        tmp = -heapq.heappop(maxH)
        if( dic[tmp] <= 0 ):
            continue
        answer[0] = tmp
        break
    while(minH):
        tmp = heapq.heappop(minH)
        if( dic[tmp] <= 0 ):
            continue
        answer[1] = tmp
        break
    return answer
