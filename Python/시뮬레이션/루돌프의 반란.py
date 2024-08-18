import sys
input = sys.stdin.readline
N, M, P, C, D = 0, 0, 0, 0, 0
turn = 0
board = []
santaArr = []

class Rudolf:
    def __init__(self, r, c):
        self.r = r
        self.c = c
rudolf = Rudolf(-1, -1)

class Santa:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.out = False
        self.freeze = 0
        self.score = 0

def scoreNotOut():
    global P, santaArr
    for i in range(1, P+1):
        santa = santaArr[i]
        if santa.out: continue
        santa.score += 1

def afterAction(r, c, crushedIdx):
    global N, santaArr
    santa = santaArr[crushedIdx]
    crushedR, crushedC = (santa.r+r), (santa.c+c)
    if not( 0 <= crushedR < N and 0 <= crushedC < N ):
        santa.out = True
        board[santa.r][santa.c] = 0
    elif board[crushedR][crushedC] != 0:
        afterAction(r, c, board[crushedR][crushedC])
    if not santa.out:
        santa.r, santa.c = crushedR, crushedC
        board[santa.r][santa.c] = crushedIdx
    return

def returnL(r1, c1, r2, c2):
    return (r1-r2)**2+(c1-c2)**2

def crush(whoMove, santaIdx, r, c):
    global N, C, D, rudolf, santaArr, turn
    santa = santaArr[santaIdx]
    santa.freeze = turn+1
    if whoMove == "r":
        santa.score += C
        crushedR, crushedC = (santa.r+r*C), (santa.c+c*C)
        if not( 0 <= crushedR < N and 0 <= crushedC < N ):
            santa.out = True
            board[santa.r][santa.c] = 0
        elif board[crushedR][crushedC] != 0:
            afterAction(r, c, board[crushedR][crushedC])
        if not santa.out:
            board[santa.r][santa.c] = 0
            santa.r, santa.c = crushedR, crushedC
            board[santa.r][santa.c] = santaIdx
    else:
        santa.score += D
        crushedR, crushedC = (rudolf.r-(r*D)), (rudolf.c-(c*D))
        if not( 0 <= crushedR < N and 0 <= crushedC < N ):
            santa.out = True
            board[santa.r][santa.c] = 0
        elif board[crushedR][crushedC] != 0 and board[crushedR][crushedC] != santaIdx:
            afterAction(-r, -c, board[crushedR][crushedC])
        if not santa.out:
            board[santa.r][santa.c] = 0
            santa.r, santa.c = crushedR, crushedC
            board[santa.r][santa.c] = santaIdx
    return

def chooseNearSanta():
    global N, P, rudolf, santaArr, turn
    santaIdx = -1
    compare = [float('inf'), -1, -1]
    for i in range(1, P+1):
        santa = santaArr[i]
        if santa.out: continue
        l = returnL(rudolf.r, rudolf.c, santa.r, santa.c)
        if l < compare[0]:
            santaIdx = i
            compare = [l, santa.r, santa.c]
        elif l == compare[0]:
            if santa.r > compare[1]:
                santaIdx = i
                compare[1] = santa.r
            elif santa.r == compare[1] and santa.c > compare[2]:
                santaIdx = i
                compare[2] = santa.c
    return santaIdx

def moveRudolf():
    global board, rudolf, santaArr, turn
    nearSantaIdx = chooseNearSanta()
    if nearSantaIdx == -1: return True
    santa = santaArr[nearSantaIdx]
    dx, dy = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, -1, 1, 1]
    compare = [float('inf'), -1, -1]
    for i in range(8):
        Rr, Rc = rudolf.r + dy[i], rudolf.c + dx[i]
        if 0 <= Rr < N and 0 <= Rc < N:
            l = returnL(Rr, Rc, santa.r, santa.c)
            if l < compare[0]:
                compare = [l, dy[i], dx[i]]
    board[rudolf.r][rudolf.c] = 0
    rudolf.r += compare[1]; rudolf.c += compare[2]
    if compare[0] == 0: crush("r", nearSantaIdx, compare[1], compare[2])
    board[rudolf.r][rudolf.c] = -1
    return False

def moveSanta():
    global N, P, rudolf, santaArr, turn
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    for i in range(1, P+1):
        santa = santaArr[i]
        if santa.out: continue
        if santa.freeze >= turn: continue
        l = returnL(rudolf.r, rudolf.c, santa.r, santa.c)
        compare = [l, -2, -1]
        for j in range(4):
            Sr, Sc = santa.r+dy[j], santa.c+dx[j]
            if (0 <= Sr < N and 0 <= Sc < N) and (board[Sr][Sc] == 0 or board[Sr][Sc] == -1):
                l = returnL(rudolf.r, rudolf.c, Sr, Sc)
                if l < compare[0]: compare = [l, dy[j], dx[j]]
        if compare[0] == 0:
            crush("s", i, compare[1], compare[2])
        elif compare[1] != -2:
            board[santa.r][santa.c] = 0
            santa.r += compare[1]; santa.c += compare[2]
            board[santa.r][santa.c] = i
    return

def main():
    global N, M, P, C, D, board, rudolf, santaArr, turn
    N, M, P, C, D = map(int, input().split(" "))
    board = [ [0]*N for _ in range(N) ]
    Rr, Rc = map(int, input().split(" "))
    rudolf.r = Rr-1; rudolf.c = Rc-1
    board[Rr-1][Rc-1] = -1
    santaArr = [Santa(-100, -100) for _ in range(P+1)]
    for _ in range(P):
        Pn, Sr, Sc = map(int, input().split(" "))
        board[Sr-1][Sc-1] = Pn
        santaArr[Pn].r = Sr-1
        santaArr[Pn].c = Sc-1
    turn = 1
    for i in range(1, M+1):
        turn = i
        if moveRudolf(): break
        moveSanta()
        scoreNotOut()
    for i in range(1, P+1):
        santa = santaArr[i]
        print(santa.score, end=" ")
main()

