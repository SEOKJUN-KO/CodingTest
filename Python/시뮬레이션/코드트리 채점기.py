import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

tools = []; waiting = {}; waitingS = set()
judging = [] # 스레드 번호 = 시작시간, 도메인
judgingS = set()
history = {} # domain = limit

def init(N, url):
    global waiting, waitingS, judging, tools
    for i in range(1, N+1): heappush(tools, i)
    judging = [ [] for _ in range(N+1) ]
    domain = url.split("/")[0]
    waiting[domain] = []
    heappush(waiting[domain], (1, 0, url)); waitingS.add(url)

def putWaiting(enter, priority, url):
    global waiting, waitingS
    if url in waitingS: return
    domain = url.split("/")[0]
    if domain not in waiting.keys(): waiting[domain] = []
    heappush(waiting[domain], (priority, enter, url)); waitingS.add(url)

def putJudging(time):
    global waiting, waitingS, history, judging, tools
    if len(tools) == 0: return # 쉬고 있는 채점기 없음
    best_prior = INF; min_enter = INF; best_domain = ''; best_url = ''
    for domain in waiting.keys():
        if len(waiting[domain]) == 0: continue # 해당 힙이 비었으면 넘어감
        # 부적절 채점 의심                                             # 현재 채점 진행 중인 도메인
        if (domain in history.keys() and history[domain] > time) or domain in judgingS: continue
        priority, enter, url = waiting[domain][0]
        if priority < best_prior: best_prior = priority; min_enter = enter; best_domain = domain; best_url = url
        if priority == best_prior and min_enter > enter: best_prior = priority; min_enter = enter; best_domain = domain; best_url = url
    
    if best_prior != INF:
        toolIdx = heappop(tools); heappop(waiting[best_domain]); waitingS.remove(best_url)
        judging[toolIdx] = [time, best_domain]; judgingS.add(best_domain)

def endJudging(time, idx):
    global judging, history, judgingS, tools
    # 해당 채점기 채점 안하는 중
    if judging[idx] == []: return
    start, domain = judging[idx]; judging[idx] = []
    history[domain] = start + 3*(time-start)
    judgingS.remove(domain)
    heappush(tools, idx)

def main():
    global waiting
    for _ in range(int(input())):
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
            for key in waiting.keys(): ans += len(waiting[key])
            print(ans)
main()
