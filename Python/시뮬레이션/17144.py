import sys
input = sys.stdin.readline

def Input():
    return map(int, input().split(" "))

def makeBoard(R):
    board = []
    for _ in range(R):
        board.append(list(Input()))
    return board

def findMachine(board):
    for y in range(len(board)):
        if board[y][0] == -1:
            return [y, y+1]

def splitDust(board, R, C):
    calBoard = [[0 for _ in range(C)] for _ in range(R)]
    
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    for y in range(R):
        for x in range(C):
            if board[y][x] > 0:
                mass = board[y][x]//5
                for i in range(4):
                    Y, X = y+dy[i], x+dx[i]
                    if 0 <= Y < R and 0 <= X < C and board[Y][X] != -1:
                        calBoard[Y][X] += mass
                        calBoard[y][x] -= mass
    for y in range(R):
        for x in range(C):
            board[y][x] += calBoard[y][x]

def suckUpsideMachine(yPoint, board, R, C):
    for y in range(yPoint-1, 0, -1):
        board[y][0] = board[y-1][0]
    for x in range(C-1):
        board[0][x] = board[0][x+1]
    for y in range(yPoint):
        board[y][C-1] = board[y+1][C-1]
    for x in range(C-1, 1, -1):
        board[yPoint][x] = board[yPoint][x-1]
    board[yPoint][1] = 0

def suckDownsideMachine(yPoint, board, R, C):
    for y in range(yPoint+1, R-1):
        board[y][0] = board[y+1][0]
    for x in range(C-1):
        board[R-1][x] = board[R-1][x+1]
    for y in range(R-1, yPoint, -1):
        board[y][C-1] = board[y-1][C-1]
    for x in range(C-1, 1, -1):
        board[yPoint][x] = board[yPoint][x-1]
    board[yPoint][1] = 0
    

def doMachine(machine, board, R, C):
    suckUpsideMachine(machine[0], board, R, C)
    suckDownsideMachine(machine[1], board, R, C)
    return

def sumMass(board, R, C):
    ans = 0
    for y in range(R):
        for x in range(C):
            if board[y][x] != -1:
                ans += board[y][x]
    return ans
            

def main():
    R, C, T = Input()
    board = makeBoard(R)
    machine = findMachine(board)
    for _ in range(T):
        splitDust(board, R, C)
        doMachine(machine, board, R, C)
    print(sumMass(board, R, C))
main()