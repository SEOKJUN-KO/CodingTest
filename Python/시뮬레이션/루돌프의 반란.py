# N*N (r,c) (1, 1) start
# M turn or 산타 모두 탈락
# 턴 끝날 때마다 탈락하지 않은 산타 1점 추가
# 1 rudolf | santas

# 루돌프 '탈락하지 않은 가장 가까운 산타'에게 1칸 돌진
# L = (r1-r2)^2 + (c1-c2)^2
# 1. r이 큰 경우
# 2. c가 큰 경우
# 상 하 좌 우 대각선

# 1번 - P번 순서대로
# 루돌프에게 거리가 '가까워지는 방향'으로 1칸 이동
# 다른 산타가 있는 칸으로 이동 불가
# 움직일 수 있는 칸 없으면 안 움직임
# 가까워 질 방법이 없다면 안 움직임
# 1. 상 2.우 3.하 4.좌

# 산타와 루돌프 같은 칸에 있다 = 충돌 -> 산타 기절 -> 밀려난 턴 + 다음 턴까지 못 움직임
# 루돌프가 움직여서 충돌 -> C 만큼 점수 + 루돌프가 이동해온 방향으로 C칸 밀림
# 산타가 움직여서 충돌 -> D 만큼 점수 + 산타는 자신이 이동해온 반대 방향으로 D칸 밀림
# 밀린 위치 게임판 밖 = 탈락

# 밀려난 칸에 다른 산타 있는 경우 = 상호작용 [ 궤도 상 말고 도착지만 ]
# 상호 작용 시 날아온 산타의 해당 방향으로 이미 있던 산타가 1칸 밀림 + 거기도 산타 있다면 반복
# 밀린 위치 게임판 밖 = 탈락

N, M, P, C, D = map(int, input().strip().split(" "))
rR, cR = map(int, input().strip().split(" "))
santasP = [[-1, -1, -1, -1]]
scoreArr = [0]
for _ in range(P):
    santasP.append(list(map(int, input().strip().split(" ")))+[-1])
    scoreArr.append(0)
    number = santasP[-1][0]
    rS = santasP[-1][1]
    cS = santasP[-1][2]
santasP.sort(key=lambda x: (-x[1], -x[2]))

def findCloseSanta():
    l, numberS = float('inf'), -1
    rr, rc = -1, -1
    for santa in santasP:
        n = santa[0]
        rS = santa[1]
        if rS == -1: continue
        cS = santa[2]
        L = (rR-rS)**2+(cR-cS)**2
        if l > L:
            l, numberS = L, n
            rr, rc = rS, cS
    return [numberS, rr, rc]

rdx, rdy = [+1, -1, +0, +0, -1, +1, +1, -1], [+0, +0, +1, -1, +1, +1, -1, -1]

def landingAfterSanta(AfterR, AfterC, moveR, moveC):
    # print("Oops", AfterR, AfterC, moveR, moveC)
    global santasP
    for i in range(len(santasP)):
        if santasP[i][1] == -1: continue
        rS, cS = santasP[i][1], santasP[i][2]
        if rS == AfterR and cS == AfterC:
            AAfterR, AAfterC = AfterR+moveR, AfterC+moveC
            if 1 <= AAfterR <= N and 1 <= AAfterC <= N:
                landingAfterSanta(AAfterR, AAfterC, moveR, moveC)
                santasP[i][1], santasP[i][2] = AAfterR, AAfterC
            else:
                santasP[i] = [i, -1, -1, -1]


def whatDirectionAndGo(r, c, m):
    global rR, cR, santasP, C, scoreArr
    l, s = float('inf'), -1
    for i in range(8):
        Y, X = rR + rdy[i], cR + rdx[i]
        if 1 <= Y <= N and 1 <= X <= N:
            L = (r-Y)**2 + (c-X)**2
            if l > L:
                l = L
                s = i
    rR, cR = rR + rdy[s], cR + rdx[s]
    for i in range(len(santasP)):
        if santasP[i][1] == -1: continue
        rS, cS = santasP[i][1], santasP[i][2]
        if rR == rS and cR == cS:
            num = santasP[i][0]
            scoreArr[santasP[i][0]] += C
            AfterR, AfterC = rR + C*rdy[s], cR + C*rdx[s]
            if 1 <=  AfterR <= N and 1 <= AfterC <= N:
                landingAfterSanta(AfterR, AfterC, rdy[s], rdx[s])
                santasP[i] = [num, AfterR, AfterC, m+1]
            else:
                santasP[i] = [num, -1, -1, -1]
            break

sdx, sdy = [+0, +1, +0, -1], [-1, +0, +1, +0]
def whatDirectionAndGoToRudolf(numofSanta, r, c, m):
    global scoreArr, D, santasP, rR, cR
    l, s = (rR-r)**2 + (cR-c)**2, -1
    # print(numofSanta, r, c)
    for i in range(4):
        Y, X = r + sdy[i], c + sdx[i]
        if 1 <= Y <= N and 1 <= X <= N:
            flag = False
            for santa in santasP:
                if santa[1] == Y and santa[2] == X:
                    flag = True
                    break
            if flag: continue
            L = (rR-Y)**2 + (cR-X)**2
            if l > L:
                l, s = L, i
    # print(l, s)
    if l != (rR-r)**2 + (cR-c)**2:
        if l == 0:
            AfterR, AfterC = rR - D*sdy[s], cR - D*sdx[s]
            scoreArr[numofSanta] += D
            if 1 <= AfterR <= N and 1 <= AfterC <= N:
                landingAfterSanta(AfterR, AfterC, -sdy[s], -sdx[s])
                santasP[numofSanta] = [numofSanta, AfterR, AfterC, m+1]
            else:
                santasP[numofSanta] = [numofSanta, -1, -1, -1]
        else:
            santasP[numofSanta] = [numofSanta, r+sdy[s], c+sdx[s], -1]

for m in range(M):
    # print(m)
    santasP.sort(key=lambda x: (-x[1], -x[2]))
    closeSanta = findCloseSanta()
    whatDirectionAndGo(closeSanta[1], closeSanta[2], m)
    # print(rR, cR, santasP)
    santasP.sort(key=lambda x: (x[0]))
    for santa in santasP:
        if santa[1] == -1: continue
        if santa[3] < m:
            whatDirectionAndGoToRudolf(santa[0], santa[1], santa[2], m)
            # print(santasP)
    # print(rR, cR, santasP)
    for i in range(len(santasP)):
        if santasP[i][1] != -1:
            scoreArr[santasP[i][0]] += 1
for i in range(1, len(scoreArr)):
    print(scoreArr[i], end=" ")
