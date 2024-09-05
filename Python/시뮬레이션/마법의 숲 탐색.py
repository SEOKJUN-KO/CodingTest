import sys
input = sys.stdin.readline
# y: 1-R x: 1-C
# 가장 위 1 / 가장 아래 R 행
# 내릴 때 정해진 출구만 가능
# c열에서 시작 / 출구는 d 방향


# 반복
# 1. 아래로 하강
# 2. 좌로 회전
# 3. 우로 회전
# 1 ...
UP = 0; RIGHT = 1; DOWN = 2; LEFT = 3
board = []
Y, X = 0, 0

class Gollem:
    def __init__(self, middleY, middleX, d):
        self.middle = [middleY, middleX]
        self.top = [middleY-1, middleX]
        self.bottom = [middleY+1, middleX]
        self.left = [middleY, middleX-1]
        self.right = [middleY, middleX+1]
        self.direction = d
    def reposition(self, middleY, middleX):
        self.middle = [middleY, middleX]
        self.top = [middleY-1, middleX]
        self.bottom = [middleY+1, middleX]
        self.left = [middleY, middleX-1]
        self.right = [middleY, middleX+1]

def moveDown(gollem):
    global board, Y, X
    leftDown = [gollem.left[0]+1, gollem.left[1]]
    bottomDown = [gollem.bottom[0]+1, gollem.bottom[1]]
    rightDown = [gollem.right[0]+1, gollem.right[1]]
    for y, x in [leftDown, bottomDown, rightDown]:
        if not (0 <= x < X and 0 <= y < Y+3): return False
        if board[y][x] != 0: return False
    
    middleY, middleX = gollem.middle[0]+1, gollem.middle[1]
    gollem.reposition(middleY, middleX)
    # print(gollem.middle)
    return True
        

def moveLeft(gollem):
    global board, Y, X
    topLeft = [gollem.top[0], gollem.top[1]-1]
    leftLeft = [gollem.left[0], gollem.left[1]-1]
    bottomLeft = [gollem.bottom[0], gollem.bottom[1]-1]
    leftLeftDown = [gollem.left[0]+1, gollem.left[1]-1]
    bottomLeftDown = [gollem.bottom[0]+1, gollem.bottom[1]-1]
    for y, x in [topLeft, leftLeft, bottomLeft, leftLeftDown, bottomLeftDown]:
        if not (0 <= x < X and 0 <= y < Y+3): return False
        if board[y][x] != 0: return False
    
    middleY, middleX = gollem.middle[0]+1, gollem.middle[1]-1
    if gollem.direction == UP: gollem.direction = LEFT
    elif gollem.direction == LEFT: gollem.direction = DOWN
    elif gollem.direction == DOWN: gollem.direction = RIGHT
    elif gollem.direction == RIGHT: gollem.direction = UP
    gollem.reposition(middleY, middleX)
    return True

def moveRight(gollem):
    global board, Y, X
    topRight = [gollem.top[0], gollem.top[1]+1]
    rightRight = [gollem.right[0], gollem.right[1]+1]
    bottomRight = [gollem.bottom[0], gollem.bottom[1]+1]
    rightRightDown = [gollem.right[0]+1, gollem.right[1]+1]
    bottomRightDown = [gollem.bottom[0]+1, gollem.bottom[1]+1]
    for y, x in [topRight, rightRight, bottomRight, rightRightDown, bottomRightDown]:
        if not (0 <= x < X and 0 <= y < Y+3): return False
        if board[y][x] != 0: return False
    
    middleY, middleX = gollem.middle[0]+1, gollem.middle[1]+1
    if gollem.direction == UP: gollem.direction = RIGHT
    elif gollem.direction == RIGHT: gollem.direction = DOWN
    elif gollem.direction == DOWN: gollem.direction = LEFT
    elif gollem.direction == LEFT: gollem.direction = UP
    gollem.reposition(middleY, middleX)
    return True

def calculate(middleY, middleX):
    global board, Y, X
    

def moves(c, d):
    global board, Y, X
    gollem = Gollem(1, c, d)
    moveDown(gollem)
    mode = 0; cnt = 0
    while(cnt < 3):
        if mode == 0:
            move = moveDown(gollem)
            if not move: mode += 1; cnt += 1
            else: cnt = 0
        elif mode == 1:
            move = moveLeft(gollem)
            if not move: mode += 1; cnt += 1
            else: cnt = 0
        else:
            move = moveRight(gollem)
            if not move: mode = 0; cnt += 1
            else: cnt = 0
    if gollem.middle[0] <= 3: board = [ [0]*X for _ in range(Y+3) ]; return 0
    for y, x in [gollem.top, gollem.middle, gollem.left, gollem.right, gollem.bottom]:
        board[y][x] = 1
    if gollem.direction == UP: board[gollem.top[0]][gollem.top[1]] = 2
    if gollem.direction == RIGHT: board[gollem.right[0]][gollem.right[1]] = 2
    if gollem.direction == DOWN: board[gollem.bottom[0]][gollem.bottom[1]] = 2
    if gollem.direction == LEFT: board[gollem.left[0]][gollem.left[1]] = 2
    
    return 0


# 바닥 붙으면 이동 끝
# 출구가 골렘과 붙어있다면, 정령은 이동 가능
# 골렘의 몸의 일부가 숲을 벗어나면, 골렘 다 지움

# 출력: 정령의 최종 위치의 행 번호의 합
# 골렘의 몸의 일부가 숲을 벗어난 경우, 더하지 않음

def init():
    global board, Y, X
    Y, X, K = map(int, input().split(" "))
    board = [ [0]*X for _ in range(Y+3) ]
    for _ in range(K):
        c, d = map(int, input().split(" "))
        moves(c-1, d)

init()
