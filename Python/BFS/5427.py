import sys
from collections import deque
input = sys.stdin.readline

# w, h = 10^3
# 10^6
# . 빈공간 / # 벽 / @ 시작 / * 불
def makeBoard(w, h):
    board = []
    for _ in range(h):
        board.append(list(input().strip()))
    return board

fires = deque()
sanggun = deque()
def search(board, w, h):
    global fires, sanggun
    for y in range(h):
        for x in range(w):
            if board[y][x] == "@":
                sanggun.append([y, x, 1])
            if board[y][x] == "*":
                fires.append([y, x, 1])

# 불이 옮겨진 칸 또는 이제 붙으려는 칸으로 이동 불가
def nextToFire(board, w, h, Y, X):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        y, x = Y+dy[i], X+dx[i]
        if 0 <= y < h and 0 <= x < w and board[y][x] == "*":
            return True
    return False

# 상근이가 있는 곳으로 불이 이동하는 거 가능 -> 상근이가 그 때 이동하면 생존
def sanggenGo(board, w, h, y, x, time):
    global sanggun
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        Y, X = y+dy[i], x+dx[i]
        if 0 <= Y < h and 0 <= X < w:
            if board[Y][X] == "*" or board[Y][X] == "#" or board[Y][X] == "@": continue
            if board[Y][X] == ".":
                if not nextToFire(board, w, h, Y, X):
                    board[Y][X] = "@"
                    sanggun.append([Y, X, time+1])
        else:
            return True
    return False

def fireGo(board, w, h, y, x, time):
    global fires
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        Y, X = y+dy[i], x+dx[i]
        if 0 <= Y < h and 0 <= X < w:
            if board[Y][X] == "#" or board[Y][X] == "*": continue
            board[Y][X] = "*"
            fires.append([Y, X, time+1])

# 이동 시 1초가 걸림    
def BFS(board, w, h):
    global fires, sanggun
    search(board, w, h)
    time = 1
    while(len(sanggun) > 0):
        while(len(sanggun) > 0 and sanggun[0][-1] == time):
            y, x, _ = sanggun.popleft()
            if sanggenGo(board, w, h, y, x, time):
                return time

        while(len(fires) > 0 and fires[0][-1] == time):
            y, x, _ = fires.popleft()
            fireGo(board, w, h, y, x, time)
        time += 1
    return -1

# T = 100
def main():
    global fires, sanggun
    T = int(input())
    for _ in range(T):
        w, h = map(int, input().split(" "))
        board = makeBoard(w, h)
        time = BFS(board, w, h)
        if time == -1: print("IMPOSSIBLE")
        else: print(time)
        fires = deque()
        sanggun = deque()
main()