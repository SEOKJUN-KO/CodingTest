import sys
from collections import deque
import itertools
from copy import deepcopy

input = sys.stdin.readline

def makeBoard(N, M):
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split(" "))))
    return board

def findDripGround(board):
    s = set()
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 2:
                s.add(str(y)+" "+str(x))
    return s

def fillGreen(dropGreenArr, originBoard, dripSet, que):
    board = deepcopy(originBoard)
    leftSet = deepcopy(dripSet)
    for st in dropGreenArr:
        y, x = map(int, st.split(" "))
        board[y][x] = 'G'
        leftSet.remove(st)
        que.append([y, x])
    return [board, leftSet]

def dropAndFillRed(dropGreenBoard, leftSet, R, que):
    ans = 0
    for brr in itertools.combinations(leftSet, R):
            newQue = deepcopy(que)
            board = deepcopy(dropGreenBoard)
            for st in brr:
                y, x = map(int, st.split(" "))
                board[y][x] = 'R'
                newQue.append([y, x])
            cnt = bfs(board, newQue)
            if ans < cnt:
                ans = cnt
    return ans


def bfs(board, que):
    nextQue = deque()
    yLimit, xLimit = len(board), len(board[0])
    cnt = 0
    while(que):
        y, x = que.popleft()
        for dy, dx in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            Y, X = y+dy, x+dx
            if (0 <= Y < yLimit) and (0 <= X < xLimit) and (board[Y][X] == "g" or board[Y][X] == "r" or board[Y][X] == 1 or board[Y][X] == 2):
                if board[y][x] == "G" and board[Y][X] == "r":
                    board[Y][X] = "F"
                    cnt += 1
                elif board[y][x] == "R" and board[Y][X] == "g":
                    board[Y][X] = "F"
                    cnt += 1
                elif board[Y][X] == 1 or board[Y][X] == 2:
                    if board[y][x] == "G":
                        board[Y][X] = "g"
                        nextQue.append([Y, X])
                    elif board[y][x] == "R":
                        board[Y][X] = "r"
                        nextQue.append([Y, X])
        if len(que) == 0:
            while(nextQue):
                nY, nX = nextQue.popleft()
                if board[nY][nX] == "g": 
                    board[nY][nX] = "G"
                    que.append([nY, nX])
                elif board[nY][nX] == "r": 
                    board[nY][nX] = "R"
                    que.append([nY, nX])

    return cnt
                
def doSomething(originBoard, dripSet: set, G, R):
    ans = 0
    for dropGreenArr in itertools.combinations(dripSet, G): # 5
        que = deque()
        boardA, leftSet = fillGreen(dropGreenArr, originBoard, dripSet, que)
        cnt = dropAndFillRed(boardA, leftSet, R, que)
        if ans < cnt:
            ans = cnt
    return ans

def main():
    N, M, G, R = map(int, input().split(" "))
    board = makeBoard(N, M)
    dripSet = findDripGround(board)
    ans = doSomething(board, dripSet, G, R)
    print(ans)
main()