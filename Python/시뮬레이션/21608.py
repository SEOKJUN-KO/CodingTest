import sys

input = sys.stdin.readline

def makeLikeData(N: int):
    like = {}
    for _ in range(N**2):
        arr = list(map(int, input().strip().split(" ")))
        idx = arr[0]
        like[idx] = set()
        for a in arr[1:]:
            like[idx].add(a)
    return like

def makeBoard(N:int):
    board = [ [0 for _ in range(N) ] for _ in range(N)]
    return board

def checkLikeScore(now, N, like, board, y, x):
    cnt = 0
    empty = 0
    for yi, xi in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        Y, X = y+yi, x+xi
        if 0 <= Y < N and 0 <= X < N:
            if board[Y][X] in like[now]:
                cnt += 1
            if board[Y][X] == 0:
                empty += 1
    return [cnt, empty]

def fillBoard(N, like, board):
    for key in like.keys():
        maxN = -1
        emptyN = -1
        bestY, bestX = -1, -1
        # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        for y in range(N):
            for x in range(N):
                if board[y][x] != 0: continue
                # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
                cnt, empty = checkLikeScore(key, N, like, board, y, x)
                if cnt > maxN:
                    maxN = cnt
                    emptyN = empty
                    bestY, bestX = y, x
                # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
                elif cnt == maxN and empty > emptyN:
                    emptyN = empty
                    bestY, bestX = y, x
        board[bestY][bestX] = key
        # for y in range(N):
        #     print(board[y])
        # print("---------------------")
    return

def calculateScore(board, like, N):
    ans = 0
    for y in range(N):
        for x in range(N):
            cnt, _ = checkLikeScore(board[y][x], N, like, board, y, x)
            if cnt == 0: ans += 0
            elif cnt == 1: ans += 1
            elif cnt == 2: ans += 10
            elif cnt == 3: ans += 100
            elif cnt == 4: ans += 1000
    return ans

def main():
    N = int(input()) # 20 -> 400
    like = makeLikeData(N)
    board = makeBoard(N)
    fillBoard(N, like, board)
    print(calculateScore(board, like, N))
main()