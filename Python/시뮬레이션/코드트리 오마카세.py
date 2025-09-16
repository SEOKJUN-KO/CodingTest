import sys
input = sys.stdin.readline

L = -1

# 100: t초에 x의 위치에 name 초밥을 넣음
sushiD = {}

def putSushi(order): # 1
    global sushiD
    t, x, name = int(order[1]), int(order[2]), order[3]
    if name not in sushiD.keys(): sushiD[name] = {}
    sushiD[name][t] = x

# 200: t초에 x의 위치에 name 손님이 오고 n 개의 초밥을 먹고 떠남
# 동일 인물 없음 

peopleD = {}
def putPerson(order): # 1
    t, x, name, n = int(order[1]), int(order[2]), order[3], int(order[4])
    peopleD[name] = [t, x, n]

# 300: t초에 초밥 회전 후, 초밥 먹은 후, 다 먹은 사람 떠나고, 사람 수, 초밥 수 출력
def countSushi():
    global sushiD
    cnt = 0
    for name in sushiD.keys():
        cnt += len(sushiD[name])
    return cnt 

def countPeople():
    global peopleD
    return len(peopleD.keys())

def sushiPlaceAtTime(putTime, putPlace, time): # 1
    global L
    return ((time - putTime) + putPlace)%L

def sushiPlaceAtPersonSit(putTime, putPlace, name): # 1
    global peopleD
    sitTime = peopleD[name][0]
    if sitTime > putTime:
        return sushiPlaceAtTime(putTime, putPlace, sitTime)
    return putPlace

def needTimeForReachPerson(A, name): #1
    global peopleD, L
    sitPlace = peopleD[name][1]
    # A가 사람이 있는 곳으로 가야함
    if A > sitPlace:
        return sitPlace + L - A
    return sitPlace - A

def timeFlowAfterSit(now, name): #1
    global peopleD
    return now - peopleD[name][0]

def timeFlowAfterPutSushi(now, putTime):
    return now-putTime

def eatSushi(name, putTime):
    global sushiD, peopleD
    
    del(sushiD[name][putTime])

    peopleD[name][2] -= 1
    
    if peopleD[name][2] == 0:
        del(peopleD[name])
        del(sushiD[name])

def canEatSushi(now):
    global sushiD, peopleD
    nameList = list(peopleD.keys())
    for name in nameList:
        if name not in sushiD.keys(): continue
        sitTime = peopleD[name][0]
        timeList = list(sushiD[name].keys())
        for putTime in timeList:
            putPlace = sushiD[name][putTime]
            A = sushiPlaceAtPersonSit(putTime, putPlace, name)
            C = needTimeForReachPerson(A, name)
            B = -1
            if putTime < sitTime:
                B = timeFlowAfterSit(now, name)
            elif putTime > sitTime:
                B = timeFlowAfterPutSushi(now, putTime)
            if (B >= C):
                eatSushi(name, putTime)

def takePicture(order):
    t = int(order[1])
    canEatSushi(t)
    cP = str(countPeople())
    cS = str(countSushi())
    print(cP+" "+cS)


def main():
    global L
    L, Q = map(int, input().strip().split(" "))
    for _ in range(Q): # 10^5
        order = list(input().strip().split(" "))
        if order[0] == "100":
            putSushi(order) #1
        elif order[0] == "200":
            putPerson(order) #1
        elif order[0] == "300":
            takePicture(order)
main()