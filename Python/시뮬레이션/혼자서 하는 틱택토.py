def checkRow(board, C):
    for y in range(3):
        cnt = 0
        for x in range(3):
            if board[y][x] == C:
                cnt += 1
        if cnt == 3: return True
    return False

def checkColumn(board, C):
    for x in range(3):
        cnt = 0
        for y in range(3):
            if board[y][x] == C:
                cnt += 1
        if cnt == 3: return True
    return False

def checkCross(board, C):
    if board[0][0] == C and board[1][1] == C and board[2][2] == C: return True
    if board[0][2] == C and board[1][1] == C and board[2][0] == C: return True
    return False

def solution(board):
    OC, XC = 0, 0
    for b in board:
        for c in b:
            if c == "O": OC += 1
            if c == "X": XC += 1
    # 번갈아 작업하지 않았다 : O == X+1 or O == X 이어야 한다.
    if not (OC == XC+1 or OC == XC): return 0
    # 선공이 승리했지만, 게임이 종료되지 않았다. => O가 3개가 채워졌지만, O != X+1 이다
    if checkRow(board, "O") or checkColumn(board, "O") or checkCross(board, "O"):
        if OC != XC+1:
            return 0
    # 후공이 승리했지만, 게임이 종료되지 않았다. => X가 3개가 채워졌지만, O != X 이다.
    if checkRow(board, "X") or checkColumn(board, "X") or checkCross(board, "X"):
        if OC != XC:
            return 0
    return 1