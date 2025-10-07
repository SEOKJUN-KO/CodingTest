from heapq import heappush, heappop

def changeToSec(timeStr):
    h, m, s = map(int, timeStr.split(":"))
    return (h*60*60) + (m*60) + s

def makeLogsArr(logs): # 3*10^5
    arr = []
    for log in logs:
        A, B = log.split("-")
        arr.append([changeToSec(A), changeToSec(B)])
    arr = sorted(arr, key = lambda x: (x[0], x[1]) )
    return arr

def makeTerms(logArr, advT, playT): # 6*10^5
    arr = []
    arr.append([0, advT])
    for s, e in logArr:
        arr.append([s, max(s+advT, playT)])
        arr.append([max(0, e-advT), e])
    arr.append([max(0, playT-advT), playT])
    arr = sorted(arr, key = lambda x: (x[0], x[1]) )
    return arr

def addTime(startT, endT, heap):
    tmp = 0
    for e, s in heap:
        tmp += min(endT, e) - max(s, startT)
    return tmp

def secToStr(time):
    h = time//3600
    h = str(h)
    if len(h) == 1: h = '0'+h
    time = time%3600
    m = time//60
    m = str(m)
    if len(m) == 1: m = '0'+m
    s = time%60
    s = str(s)
    if len(s) == 1: s = '0'+s
    return h+":"+m+":"+s

def printAll(heap):
    for e, s in heap:
        print([secToStr(e), secToStr(s)], end=" ")

def calculate(play_time, adv_time, logs):
    logArr = makeLogsArr(logs)
    advT = changeToSec(adv_time)
    playT= changeToSec(play_time)
    terms = makeTerms(logArr, advT, playT)
    
    heap = []
    answer = [0, changeToSec('100:0:0')]
    lastP = 0
    for i in range(len(terms)): #6*10^6
        s, e = terms[i]
        while(heap and heap[0][0] < s):
            heappop(heap)
        while(lastP < len(logArr) and logArr[lastP][0] <= s+advT ):
            ee = logArr[lastP][1]
            ss = logArr[lastP][0]
            heappush(heap, (ee, ss))
            lastP += 1
        tmp = addTime(s, s+advT, heap) # -> 이게 문제일수도?
        if answer[0] < tmp: 
            answer = [tmp, secToStr(s)]
        if s+advT >= playT: break
    return answer[1]
    
def solution(play_time, adv_time, logs):
    return calculate(play_time, adv_time, logs)