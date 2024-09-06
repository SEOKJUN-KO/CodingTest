import sys
from collections import deque
input = sys.stdin.readline

UP = 0; RIGHT = 1; DOWN = 2; LEFT = 3
board = []
Y, X = 0, 0
turn = 0

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
    que = deque()
    que.append([middleY, middleX, board[middleY][middleX]])
    visit = set([]); visit.add((middleY, middleX))
    cnt = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while(que):
        y, x, m = que.popleft()
        if cnt < y: cnt = y
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not (0 <= ny < Y+3 and 0 <= nx < X): continue
            if type(m) == type("str") and (ny, nx) not in visit and board[ny][nx] != 0:
                que.append([ny, nx, board[ny][nx]])
                visit.add((ny, nx))
            elif (ny, nx) not in visit and (board[ny][nx] == int(m) or board[ny][nx] == str(m)):
                que.append([ny, nx, board[ny][nx]])
                visit.add((ny, nx))
    return cnt-2
            
def moves(c, d):
    global board, Y, X, turn
    gollem = Gollem(1, c, d)
    while(True):
        if moveDown(gollem): continue
        if moveLeft(gollem): continue
        if moveRight(gollem): continue
        break
    if gollem.middle[0] <= 3: board = [ [0]*X for _ in range(Y+3) ]; return 0
    for y, x in [gollem.top, gollem.middle, gollem.left, gollem.right, gollem.bottom]: board[y][x] = turn
    if gollem.direction == UP: board[gollem.top[0]][gollem.top[1]] = str(turn)
    if gollem.direction == RIGHT: board[gollem.right[0]][gollem.right[1]] = str(turn)
    if gollem.direction == DOWN: board[gollem.bottom[0]][gollem.bottom[1]] = str(turn)
    if gollem.direction == LEFT: board[gollem.left[0]][gollem.left[1]] = str(turn)
    return calculate(gollem.middle[0], gollem.middle[1])


def init():
    global board, Y, X, turn
    Y, X, K = map(int, input().split(" "))
    board = [ [0]*X for _ in range(Y+3) ]
    ans = 0
    for i in range(3, K+3):
        turn = i
        c, d = map(int, input().split(" "))
        ans += moves(c-1, d)
    print(ans)
init()
