import sys
input = sys.stdin.readline

def makeBoard(N):
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split(" "))))
    return board

def rainMagic(N):
    cloud = [ [N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1] ]
    return cloud

def first(cloud, d, s, N):
    dy, dx = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
    for i in range(len(cloud)):
        Y, X = cloud[i]
        for _ in range(s):
            Y, X = Y+dy[d], X+dx[d]
            if (Y <= -1): Y = N-1
            if (Y >= N): Y = 0
            if (X <= -1): X = N-1
            if (X >= N): X = 0
        cloud[i] = [Y, X]

def second(cloud, board, usedCloud):
    for y, x in cloud:
        board[y][x] += 1
        if y not in usedCloud.keys():
            usedCloud[y] = {}
        usedCloud[y][x] = True

def fourth(cloud, board, N):
    dy, dx = [-1, -1, 1, 1], [-1, 1, 1, -1]
    for i in range(len(cloud)):
        y, x = cloud[i]
        cnt = 0
        for j in range(4):
            Y, X = y+dy[j], x+dx[j]
            if (0 <= Y < N and 0 <= X < N and board[Y][X] > 0):
                cnt += 1
        board[y][x] += cnt

def fifth(usedCloud: dict, cloud, board, N):
    for y in range(N):
        for x in range(N):
            if board[y][x] >= 2 and (y not in usedCloud.keys() or x not in usedCloud[y].keys()):
                cloud.append([y, x])
                board[y][x] -= 2

def doSteps(board, cloud: list, N):
    d, s = map(int, input().split(" "))
    first(cloud, d-1, s, N)
    usedCloud = {}
    second(cloud, board, usedCloud)
    fourth(cloud, board, N)
    cloud.clear()
    fifth(usedCloud, cloud, board, N)
    
def calculate(board, N):
    cnt = 0
    for y in range(N):
        cnt += sum(board[y])
    return cnt
  

def main():
    N, M = map(int, input().split(" "))
    board = makeBoard(N)
    cloud = rainMagic(N)
    for _ in range(M):
        doSteps(board, cloud, N)
    print(calculate(board, N))
main()