from collections import deque 

def checkInTwo(board, y, x):
    visit = set()
    visit.add(str(y)+" "+str(x))
    que = deque()
    que.append([y, x])
    
    while(que):
        ny, nx = que.popleft()
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            Y, X = ny+dy, nx+dx
            key = str(Y)+" "+str(X)
            if 0 <= Y < 5 and 0 <= X < 5 and board[Y][X] != 'X' and key not in visit and abs(y-Y)+abs(x-X) <= 2:
                if board[Y][X] == 'P': return True
                visit.add(key)
                que.append([Y, X])
    return False
                
                

def calculate(board):
    for y in range(5):
        for x in range(5):
            if board[y][x] == "P":
                if checkInTwo(board, y, x): return 0
    return 1

def solution(places):
    ans = []
    for p in places:
        ans.append(calculate(p))
    return ans