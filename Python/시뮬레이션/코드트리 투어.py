import sys
import copy
from heapq import heappush, heappop
input = sys.stdin.readline

boardDict = []
minCostDict = {}
minCost = []
n = 0
bestHeap = []
travelDict = {}
class Travle:
    def __init__(self, idx, revenue, dest):
        global minCost, bestHeap
        self.idx = idx
        self.revenue = revenue
        self.dest = dest
        self.cost = minCost[dest]
        if self.revenue < self.cost: return
        heappush(bestHeap, (-(self.revenue-self.cost), self.idx))
        
    def changeStart(self):
        global minCost, bestHeap
        self.cost = minCost[self.dest]
        if self.revenue < self.cost: return
        heappush(bestHeap, (-(self.revenue-self.cost), self.idx))

def calculateMinLength(start):
    global minCost, minCostDict, n, boardDict
    if start in minCostDict:
        minCost = minCostDict[start]
        return
    minCost = [ float('inf') for _ in range(n) ]
    minCost[start] = 0
    heap = []; heappush(heap, [start, 0])
    while(heap):
        now, weight = heappop(heap)
        if minCost[now] != weight: continue
        for nxt in boardDict[now].keys():
            w = boardDict[now][nxt]
            if w+weight < minCost[nxt]:
                minCost[nxt] = w+weight
                heappush(heap, [nxt, minCost[nxt]])
    minCostDict[start] = copy.deepcopy(minCost)

def setting(inp):
    global boardDict, n
    n, m = inp[1], inp[2]
    boardDict = [ {} for _ in range(n) ]
    idx = 3
    while(idx < len(inp)):
        v, u, w = inp[idx], inp[idx+1], inp[idx+2]
        if u not in boardDict[v].keys():
            boardDict[v][u] = float('inf')
            boardDict[u][v] = float('inf')
        if boardDict[v][u] > w: boardDict[v][u] = w
        if boardDict[u][v] > w: boardDict[u][v] = w
        idx += 3
    calculateMinLength(0)

Q = int(input())
for _ in range(Q):
    inp = list(map(int, input().split(" ")))
    if inp[0] == 100: setting(inp)
    elif inp[0] == 200:
        idx, revenue, dest = inp[1], inp[2], inp[3]
        travel = Travle(idx, revenue, dest)
        travelDict[idx] = travel
    elif inp[0] == 300:
        idx = inp[1]
        if idx in travelDict.keys(): del(travelDict[idx])
    elif inp[0] == 400:
        if len(bestHeap) == 0: print(-1)
        else:
            while(True):
                w, idx = heappop(bestHeap)
                if idx in travelDict.keys():
                    print(idx)
                    del(travelDict[idx])
                    break
                if len(bestHeap) == 0:
                    print(-1)
                    break
    elif inp[0] == 500:
        start = inp[1]
        bestHeap = []
        calculateMinLength(start)
        for key in travelDict.keys(): travelDict[key].changeStart()
