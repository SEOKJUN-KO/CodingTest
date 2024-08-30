import sys
from heapq import heappush, heappop
input = sys.stdin.readline

class Rabbit:
    def __init__(self, rid, d):
        self.hop = 0
        self.y = 0; self.x = 0
        self.rid = rid
        self.length = d
        self.score = 0

N, M, P = 0, 0, 0
heap = []
rabbitDic = {}
scoreTotal = 0
def init(order):
    global N, M, P, heap, rabbitDic
    N, M, P = order[1], order[2], order[3]
    for i in range(P):
        rid, d = order[4+2*i], order[5+2*i]
        heappush(heap, (0, 0, 0, 0, rid))
        rabbitDic[rid] = Rabbit(rid, d)

def updateRabbit(rid, Y, X):
    global rabbitDic, heap, scoreTotal
    rabbitDic[rid].hop += 1
    rabbitDic[rid].y = Y
    rabbitDic[rid].x = X
    heappush(heap, (rabbitDic[rid].hop, Y+X, Y, X, rid))
    scoreTotal += (Y+X+2)
    rabbitDic[rid].score -= (Y+X+2)

def pickAndGiveScore(store, score):
    global rabbitDic
    heap = []
    for rid in store:
        rabbit = rabbitDic[rid]
        hop = rabbit.hop
        Y = rabbit.y
        X = rabbit.x
        heappush(heap, (-(Y+X), -Y, -X, -rid))
    rid = -heap[0][3]
    rabbitDic[rid].score += (score)

def pickAndGo(K, S): # 4*10^3
    global N, M, P, heap, rabbitDic
    store = set([])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for _ in range(K): # 10^2
        hop, YpX, y, x, rid = heappop(heap) # log(2000) = 10
        store.add(rid)
        storeY, storeX = -1, -1
        l = rabbitDic[rid].length
        for i in range(4): # 4
            CX = l%((M-1)*2); DX = dx[i]; X = x
            CY = l%((N-1)*2); DY = dy[i]; Y = y; #
            while(CX > 0 and DX != 0): # 3
                if DX == 1:
                    if (M-1)-X <= CX: CX -= (M-1)-X; X = M-1; DX = -1
                    else: X = X+CX; break
                else:
                    if X <= CX: CX -= X; X = 0; DX = 1
                    else: X = X-CX; break
            while(CY > 0 and DY != 0): # 3
                if DY == 1:
                    if (N-1)-Y <= CY: CY -= (N-1)-Y; Y = N-1; DY = -1
                    else: Y = Y+CY; break
                else:
                    if Y <= CY: CY -= Y; Y = 0; DY = 1
                    else: Y = Y-CY; break
                    
            if Y+X > storeX+storeY: storeY, storeX = Y, X
            elif Y+X == storeX+storeY:
                if Y > storeY: storeY, storeX = Y, X
                elif Y == storeY and X > storeX: storeY, storeX = Y, X
        updateRabbit(rid, storeY, storeX)
    pickAndGiveScore(store, S)
            
def changeL(rid, L):
    global rabbitDic
    rabbitDic[rid].length *= L

def pickBest():
    global scoreTotal, rabbitDic
    tmp = 0
    for rid in rabbitDic.keys():
        rabbit = rabbitDic[rid]
        if tmp < scoreTotal + rabbit.score: tmp = scoreTotal + rabbit.score
    print(tmp)

def main():
    for _ in range(int(input())):
        order = list(map(int, input().split(" ")))
        if order[0] == 100:
            init(order)
        elif order[0] == 200:
            K, S = order[1], order[2]
            pickAndGo(K, S)
        elif order[0] == 300:
            rid = order[1]; L = order[2]
            changeL(rid, L)
        elif order[0] == 400:
            pickBest()
main()
