import sys
from collections import deque
input = sys.stdin.readline

top = [-1, 0]; bottom = [1, 0]; left = [0, -1]; right = [0, 1]; mid = [0, 0]

R, C, K = map(int, input().split(" "))
board = [ [0]*C for _ in range(R+3) ]

class Gollem:
    def __init__(self, idx, x, d):
        global R
        self.idx = idx
        self.midX = x
        self.midY = 1
        self.direct = d
    def goDown(self):
        global R, C, board
        for d in [[left, bottom], [bottom, bottom], [right, bottom]]:
            dy, dx = 0, 0
            for y, x in d: dy += y; dx += x
            Y, X = self.midY+dy, self.midX+dx
            if not(0 <= Y < R+3 and 0 <= X < C): return False
            if board[Y][X] != 0: return False
        self.midY += 1;
        return True
    def rotateLeft(self):
        global R, C, board
        for d in [[top, left], [left, left], [bottom, left], [left, left, bottom], [bottom, left, bottom]]:
            dy, dx = 0, 0
            for y, x in d: dy += y; dx += x
            Y, X = self.midY+dy, self.midX+dx
            if not( 0 <= Y < R+3 and 0 <= X < C): return False
            if board[Y][X] != 0: return False
        self.midY += 1; self.midX -= 1;
        self.direct -= 1;
        if self.direct == -1: self.direct = 3
        return True
    def rotateRight(self):
        global R, C, board
        for d in [[top, right], [right, right], [bottom, right], [right, right, bottom], [bottom, right, bottom]]:
            dy, dx = 0, 0
            for y, x in d: dy += y; dx += x
            Y, X = self.midY+dy, self.midX+dx
            if not( 0 <= Y < R+3 and 0 <= X < C): return False
            if board[Y][X] != 0: return False
        self.midY += 1; self.midX += 1;
        self.direct += 1;
        if self.direct == 4: self.direct = 0
        return True
    
    def move(self):
        global R, C, board
        while(True):
            if self.goDown(): continue
            if self.rotateLeft(): continue
            if self.rotateRight(): continue
            break
        if self.midY <= 3:
            board = [ [0]*C for _ in range(R+3) ]
            return False
        else :
            for dy, dx in [top, left, mid, right, bottom]:
                Y, X = self.midY+dy, self.midX+dx
                if self.direct == 0 and [dy, dx] == top: board[Y][X] = -self.idx
                elif self.direct == 1 and [dy, dx] == right: board[Y][X] = -self.idx
                elif self.direct == 2 and [dy, dx] == bottom: board[Y][X] = -self.idx
                elif self.direct == 3 and [dy, dx] == left: board[Y][X] = -self.idx
                else: board[Y][X] = self.idx
        return True
    def calculate(self):
        global R, C, board
        que = deque()
        que.append([self.midY, self.midX, self.idx])
        visit = set([]); visit.add((self.midY, self.midX))
        dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
        ret = self.midY
        while(que):
            ny, nx, number = que.popleft()
            for i in range(4):
                Y, X = ny+dy[i], nx+dx[i]
                if (Y, X) in visit: continue
                if not( 0 <= Y < R+3 and 0 <= X < C): continue
                if (number < 0 or (board[Y][X] == number) or -1*board[Y][X] == number) and board[Y][X] != 0:
                    que.append([Y, X, board[Y][X]]); visit.add((Y, X))
                    if ret < Y: ret = Y
        return ret-2
ans = 0
for i in range(2, K+2):
    c, d = map(int, input().split(" "))
    gollem = Gollem(i, c-1, d)
    if gollem.move():
        ans += gollem.calculate()
print(ans)
