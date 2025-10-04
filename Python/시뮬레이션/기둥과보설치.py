poleD = {}
boD = {}


def canAddBo(y, x): # 검증
    global poleD, boD
    if y == 0: return False # 바닥에 지붕을 못 놓는다
    if y-1 in poleD.keys() and x in poleD[y-1]:# 왼쪽 끝이 기둥 위
        return True
    elif y-1 in poleD.keys() and x+1 in poleD[y-1]:# 오른쪽 끝이 기둥 위
        return True
    elif y in boD.keys() and ( x-1 in boD[y] and x+1 in boD[y] ):# 양쪽 끝 부분이 다른 보와 동시 연결
        return True
    return False

def canAddPole(y, x): # 검증
    global poleD, boD
    if y == 0: # 바닥 위에 있기
        return True
    else:
        if y-1 in poleD.keys() and x in poleD[y-1]: # 다른 기둥 위에 있기
            return True
        elif y in boD.keys() and x in boD[y]: # 보의 왼쪽 끝
            return True
        elif y in boD.keys() and x-1 in boD[y]: # 보의 오른쪽 끝
            return True
    return False

# 기둥 
def addPole(y, x): # 검증
    global poleD
    if y not in poleD.keys(): poleD[y] = set()
    poleD[y].add(x)

def doPole(y, x, mode):
    global poleD, boD
    if mode == 0: # delete
        if ( y not in poleD.keys() ) or ( y in poleD.keys() and x not in poleD[y]): return
        poleD[y].remove(x) 
        if (y+1 in poleD.keys() and x in poleD[y+1]) and (not canAddPole(y+1, x) ):# 위에 기둥이 있다면, 문제가 없어야 한다.
            poleD[y].add(x)
        elif (y+1 in boD.keys() and x-1 in boD[y+1]) and (not canAddBo(y+1, x-1) ):# 기둥 왼쪽 위에 붙은 보가 있다면, 문제가 없어야 한다.
            poleD[y].add(x)
        elif (y+1 in boD.keys() and x in boD[y+1]) and (not canAddBo(y+1, x) ):# 기둥 오른쪽 위에 붙은 보가 있다면, 문제가 없어야 한다.
            poleD[y].add(x)
        if len(poleD[y]) == 0: del(poleD[y])
    elif mode == 1 and canAddPole(y, x): addPole(y, x)

# 보
def addBo(y, x): # 검증
    global boD
    if y not in boD.keys(): boD[y] = set()
    boD[y].add(x)

def doBo(y, x, mode):
    global poleD, boD
    if mode == 0: # 보를 삭제할 때
        if ( y not in boD.keys() ) or ( y in boD.keys() and x not in boD[y]): return
        boD[y].remove(x)
        if (y in boD.keys() and x-1 in boD[y]) and ( not canAddBo(y, x-1) ):# 왼쪽에 붙은 보가 있다면, 문제가 없어야 한다.
            boD[y].add(x)
        elif (y in boD.keys() and x+1 in boD[y]) and ( not canAddBo(y, x+1) ):# 오른쪽에 붙은 보가 있다면, 문제가 없어야 한다.
            boD[y].add(x)
        elif (y in poleD.keys() and x in poleD[y]) and ( not canAddPole(y, x) ):# 보 왼쪽 끝 위에 기둥이 있다면, 문제가 없어야 한다.
            boD[y].add(x)
        elif (y in poleD.keys() and x+1 in poleD[y]) and ( not canAddPole(y, x+1) ):# 보 오른쪽 끝 위에 기둥이 있다면, 문제가 없어야 한다.
            boD[y].add(x)
        if len(boD[y]) == 0: del(boD[y])
    elif mode == 1 and canAddBo(y, x): # add
        addBo(y, x)
            

def build(n, build_frame):
    global poleD, boD
    for frame in build_frame:
        x, y, obj, mode = frame
        if obj == 0: doPole(y, x, mode)
        else: doBo(y, x, mode)
    
    answer = []
    for y in poleD.keys():
        for x in poleD[y]:
            answer.append([x, y, 0])
    for y in boD.keys():
        for x in boD[y]:
            answer.append([x, y, 1])
    if len(answer) > 0:
        answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer

def solution(n, build_frame):
    return build(n, build_frame)