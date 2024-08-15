import sys
import copy
from collections import deque
input = sys.stdin.readline

k, m = 0, 0
board = []
arr = []; idx = 0

def rotate(copyB, mx, my):
    tmp = []
    for y in range(my+1, my-2, -1):
        tmp.append( copyB[y][mx-1] )
    tmp.append(copyB[my+1][mx]); tmp.append(copyB[my-1][mx])
    for y in range(my+1, my-2, -1):
        tmp.append(copyB[y][mx+1])
    idx = 0
    for y in range(my-1, my+2):
        for x in range(mx-1, mx+2):
            if y == my and x == mx: continue
            copyB[y][x] = tmp[idx]
            idx += 1
    return

def fillTreasure(copyB):
    global arr, idx
    for x in range(5):
        for y in range(4, -1, -1):
            if copyB[y][x] == 0:
                copyB[y][x] = arr[idx]
                idx = (idx+1)%(len(arr))
    return

def gainTreasure(copyB, flag):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    sumCnt = 0; total = 0
    for y in range(5):
        for x in range(5):
            if copyB[y][x] == 0: continue
            que = deque(); que.append([x, y]);
            tmp = copyB[y][x]; copyB[y][x] = 0; arr = [[x, y]]
            while(que):
                nx, ny = que.popleft()
                for i in range(4):
                    X, Y = nx+dx[i], ny+dy[i]
                    if 0 <= X < 5 and 0 <= Y < 5 and tmp == copyB[Y][X]:
                        que.append([X, Y])
                        copyB[Y][X] = 0
                        arr.append([X, Y])
            if len(arr) < 3:
                for nx, ny in arr:
                    copyB[ny][nx] = tmp
            else:
                sumCnt += len(arr)
    if sumCnt >= 3:
        fillTreasure(copyB)
        if flag:
            total = gainTreasure(copyB, True) + sumCnt
        else:
            total = sumCnt
    return total

# 1차 가치 최대, 각도 최소, 작은 x, 작은 y
def logic(board):
    global idx
    storeIdx = idx
    compare = [0, 5, 5, 3]
    storeBoard = []
    for y in range(1, 4):
        for x in range(1, 4):
            for i in range(3):
                copyB = copy.deepcopy(board)
                for _ in range(i+1):
                    rotate(copyB, x, y)
                idx = storeIdx
                cnt = gainTreasure(copyB, False)
                if cnt > compare[0]:
                    compare = [cnt, y, x, i]
                    storeBoard = copy.deepcopy(copyB)
                elif cnt == compare[0]:
                    if i < compare[3]:
                        compare = [cnt, y, x, i]
                        storeBoard = copy.deepcopy(copyB)
                    elif i == compare[3]:
                        if x < compare[2]:
                            compare = [cnt, y, x, i]
                            storeBoard = copy.deepcopy(copyB)
                        elif x == compare[2] and y < compare[1]:
                            compare = [cnt, y, x, i]
                            storeBoard = copy.deepcopy(copyB)
    if compare[0] > 0:
        idx = storeIdx + compare[0]
        cnt = gainTreasure(storeBoard, True)
        print(compare[0]+cnt, end = " ")
        idx += cnt
        return [False, storeBoard]
    return [True, board]
            

def main():
    global board, arr
    k, m = map(int, input().split(" "))
    for _ in range(5):
        board.append(list(map(int, input().split(" "))))
    arr = list(map(int, input().split(" ")))
    for _ in range(k):
        ret = logic(board)
        if ret[0]: break
        board = ret[1]
        
    
main()
