def changeToSec(timeStr):
    h, m, s = map(int, timeStr.split(":"))
    return (h*60*60) + (m*60) + s

def makeLogsArr(logs):
    arr = []
    for log in logs:
        A, B = log.split("-")
        arr.append([changeToSec(A), changeToSec(B)])
    arr = sorted(arr, key = lambda x: (x[0], x[1]) )
    return arr

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

def calculate(play_time, adv_time, logs):
    logArr = makeLogsArr(logs)
    advT = changeToSec(adv_time)
    playT= changeToSec(play_time)
    
    if advT >= playT: return "00:00:00"
    
    times = [0 for _ in range(playT+2)]
    for s, e in logArr:
        times[s] += 1
        if e < playT:     
            times[e] -= 1  
    
    dp = [0 for _ in range(playT+2)]
    dp[0] = times[0]
    for i in range(1, playT+1):
        dp[i] = dp[i-1] + times[i]
    
    answer = [-1, playT]
    sumT = 0

    for i in range(advT):
        sumT += dp[i]
    if sumT > answer[0]:
        answer = [sumT, 0]
    
    for t in range(advT, playT):
        sumT += dp[t]
        sumT -= dp[t-advT]
        if sumT > answer[0]:
            answer = [sumT, t-advT+1]
        
    return secToStr(answer[1])
    
def solution(play_time, adv_time, logs):
    return calculate(play_time, adv_time, logs)