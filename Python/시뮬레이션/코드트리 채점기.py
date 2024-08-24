import sys
import heapq
input = sys.stdin.readline

tools = [];
waiting = {}; waitingS = set(); waitingD = {}
judging = [] # 스레드 번호 = 시작시간, 도메인
judgingS = set()
history = {} # domain = limit

def init(N, url):
    global waiting, waitingS, judging, tools
    tools = []
    for i in range(1, N+1):
        heapq.heappush(tools, i)
    judging = [ [] for _ in range(N+1) ]
    domain = url.split("/")[0]
    waiting[domain] = []
    waiting[domain].append( (1, 0, url) )
    waitingS.add(url)

def putWaiting(time, priority, url):
    global waiting, waitingS
    if url in waitingS: return
    domain = url.split("/")[0]
    if domain not in waiting.keys(): waiting[domain] = []
    heapq.heappush(waiting[domain], (priority, time, url)); waitingS.add(url)

def putJudging(time):
    global waiting, waitingS, history, judging, tools, waitingD
    if len(tools) == 0: return
    tmp = []
    for domain in waitingD.keys():
        if domain in judgingS: continue
        limit = 0
        if domain in history.keys(): limit = history[domain]
        while(waitingD[domain]):
            enter, priority, url = heapq.heappop(waitingD[domain])
            if len(waiting[domain]) == 0: waiting[domain] = []
            if limit <= time: heapq.heappush(waiting[domain], (priority, -enter, url))
            else: heapq.heappush(waitingD[domain], (enter, priority, url)); break
        if len(waitingD[domain]) == 0: tmp.append(domain)
    for t in tmp: del(waitingD[t])

    tmp = [float('inf'), float('inf'), ""]
    for domain in waiting.keys():
        if domain in judgingS: continue
        while(waiting[domain]):
            priority, enter, url = heapq.heappop(waiting[domain]);
            limit = 0
            if domain in history.keys(): limit = history[domain]
            if limit <= time:
                if tmp[0] >= priority and tmp[1] > enter:
                    if tmp[0] != float('inf'): heapq.heappush(waiting[tmp[2].split("/")[0]], (-tmp[1], tmp[0], tmp[2]))
                    tmp = [priority, enter, url]
                else:
                    if domain not in waitingD.keys(): waitingD[domain] = []
                    heapq.heappush(waitingD[domain], (-enter, priority, url))
                break
            else:
                if domain not in waitingD.keys(): waitingD[domain] = []
                heapq.heappush(waitingD[domain], (-enter, priority, url))
    if tmp[0] != float('inf'):
        priority, enter, url = tmp
        domain = url.split("/")[0]
        tool = heapq.heappop(tools)
        if len(waiting[domain]) == 0: del(waiting[domain])
        waitingS.remove(url)
        judging[tool] = [time, domain]; judgingS.add(domain)
        # print("waiting", waiting)
        # print(judging, judgingS)

def endJudging(time, idx):
    global judging, history, judgingS, tools
    if judging[idx] == []: return
    start, domain = judging[idx]; judging[idx] = []
    history[domain] = start+3*(time-start)
    judgingS.remove(domain)
    heapq.heappush(tools, idx)
    # print(400, history)

def main():
    global waiting
    for _ in range(int(input())): # 5*10^5
        order = input().strip().split(" ")
        if order[0] == "100":
            init(int(order[1]), order[2])
        elif order[0] == "200":
            time = int(order[1]); priority = int(order[2]); url = order[3]
            putWaiting(time, priority, url)
        elif order[0] == "300":
            putJudging(int(order[1]))
        elif order[0] == "400":
            time = int(order[1]); idx = int(order[2])
            endJudging(time, idx)
        else:
            ans = 0
            for domain in waiting.keys(): ans += len(waiting[domain])
            for domain in waitingD.keys(): ans += len(waitingD[domain])
            print(ans)
main()
