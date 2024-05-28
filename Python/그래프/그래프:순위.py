# n = 10^2

def solution(n, results):
    board = [ [False]*(n+1) for _ in range(n+1) ]
    for r in results:
        win, lose = r
        board[win][lose] = True
    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if board[i][m] and board[m][j]:
                    board[i][j] = True
    answer = 0
    for i in range(1, n+1):
        tmp = 0
        for j in range(1, n+1):
            if board[i][j] or board[j][i]:
                tmp += 1
        if tmp == n-1: answer += 1
    
    return answer
