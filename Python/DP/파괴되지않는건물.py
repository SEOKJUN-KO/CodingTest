attackB = []

def addSkill(skills, X): # 10^4
    global attackB
    for skill in skills: # 100
        type, r1, c1, r2, c2, degree = skill
        if type == 1:
            degree = -degree
        for y in range(r1, r2+1): # 100
            attackB[y][c1] += degree
            if c2+1 < X:
                attackB[y][c2+1] += -degree
    
def calculate(board):
    global attackB
    Y = len(board)
    X = len(board[0])
    cnt = 0
    for y in range(Y): # 100
        alpha = 0
        for x in range(X): # 100
            alpha += attackB[y][x]
            board[y][x] += alpha
            if board[y][x] >= 1: cnt += 1
    return cnt
            
    
def solution(board, skill):
    global attackB
    for y in range(len(board)):
        attackB.append([])
        for x in range(len(board[0])):
            attackB[y].append(0)
             
    addSkill(skill, len(board[0])) #10^4
    return calculate(board)