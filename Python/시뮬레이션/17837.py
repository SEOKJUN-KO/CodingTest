import sys
input = sys.stdin.readline


horseInfo = []
upSide = {}
directToP = {'u': [-1, 0], 'd': [1, 0], 'l': [0, -1], 'r': [0, 1]}

def makeBoard(N):
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split(" "))))
    return board

def setHorses(K):
    global horseInfo, upSide
    for i in range(K):
        Y, X, d = map(int, input().split(" "))
        y, x = Y-1, X-1
        if d == 1:
            horseInfo.append([y, x, 'r'])
        elif d == 2:
            horseInfo.append([y, x, 'l'])
        elif d == 3:
            horseInfo.append([y, x, 'u'])
        else:
            horseInfo.append([y, x, 'd'])
        upSide[i] = -1

def checkNext(board, N, idx):
    global horseInfo, directToP
    y, x, d = horseInfo[idx]
    p = directToP[d]
    Y, X = y+p[0], x+p[1]
    if ( 0 <= Y < N and 0 <= X < N):
        if board[Y][X] == 0: return "white"
        if board[Y][X] == 1: return "red"
        if board[Y][X] == 2: return "blue"
    else:
        return "out"
    
def haveHorse(Y, X, idx):
    global horseInfo
    for i in range(len(horseInfo)):
        y, x, _ = horseInfo[i]
        if y == Y and x == X:
            current = i
            tmp = -1
            while(current != -1):
                tmp = current
                current = upSide[current]
            upSide[tmp] = idx
            break

def byBotton(idx):
    global upSide
    for i in range(len(upSide)):
        if upSide[i] == idx:
            upSide[i] = -1 
            return
    
def move(idx, Y, X):
    global horseInfo, upSide
    byBotton(idx)
    haveHorse(Y, X, idx)
    current = idx
    while(current != -1):
        horseInfo[current][0], horseInfo[current][1] = Y, X
        current = upSide[current]
    # print(upSide)

def reverseStack(idx):
    current = idx
    arr = []
    while( current != -1):
        arr.append(current)
        current = upSide[current]

    for i in range(len(arr)-1, 0, -1):
        up, down = arr[i], arr[i-1]
        upSide[up] = down
    upSide[idx] = -1
    return arr[-1]

def reverseDirection(d):
    if d == "u": return "d"
    if d == "d": return "u"
    if d == "l": return "r"
    if d == "r": return "l"

def countStack(K):
    global upSide
    used = [ False for _ in range(K) ]
    for idx in range(K):
        if not used[idx]:
            used[idx] = True
            count = 0
            current = idx
            while(current != -1):
                current = upSide[current]
                count += 1
            if count >= 4:
                return True
    return False

def Turn(board, N, K):
    global horseInfo, directToP
    for t in range(1, 1001):
        for i in range(K):
            # print("t, i", [t, i])
            next = checkNext(board, N, i)
            y, x, d = horseInfo[i]
            if next == "white":
                p = directToP[d]
                Y, X = y+p[0], x+p[1]
                move(i, Y, X)
            elif next == "red":
                p = directToP[d]
                Y, X = y+p[0], x+p[1]
                bottom = reverseStack(i)
                move(bottom, Y, X)
            elif next == "blue" or "out":
                D = reverseDirection(d)
                horseInfo[i][2] = D
                nnext = checkNext(board, N, i)
                p = directToP[D]
                Y, X = y+p[0], x+p[1]
                if nnext == "white":
                    move(i, Y, X)
                elif nnext == "red":
                    bottom = reverseStack(i)
                    move(bottom, Y, X)
            if countStack(K):
                return t
    return -1

def main():
    global horseInfo, upSide
    N, K = map(int, input().split(" "))
    board = makeBoard(N)
    setHorses(K)
    ans = Turn(board, N, K)
    print(ans)
main()