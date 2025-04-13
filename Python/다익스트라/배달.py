# Dijkstra
from collections import deque
def solution(N, road, K):
    ans = 0
    board = [ [ float('inf') for _ in range(N+1) ] for _ in range(N+1) ] 
    for a, b, m in road:
        board[a][b] = min(board[a][b], m)
        board[b][a] = min(board[b][a], m)
    
    lenArr = [ float('inf') for _ in range(N+1) ]
    lenArr[1] = 0
    
    que = deque()
    que.append([1, lenArr[1]])
    
    while(que):
        now, leng = que.popleft()
        if lenArr[now] != leng: continue
        
        for i in range(1, N+1):
            if board[now][i] != float('inf') and board[now][i] + leng < lenArr[i]:
                lenArr[i] = board[now][i] + leng
                que.append([i, lenArr[i]])
    for l in lenArr:
        if l <= K: 
            ans += 1
    return ans


# floyd-warshall
def solution(N, road, K):
    ans = 1
    board = [ [float('inf') for _ in range(N+1)] for _ in range(N+1)]
    
    for a, b, m in road:
        board[a][b] = min(m, board[a][b])
        board[b][a] = min(m, board[b][a])
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if board[i][k] + board[k][j] < board[i][j]:
                    board[i][j] = board[i][k] + board[k][j]
    for i in range(2, N+1):
        if board[1][i] <= K:
            ans += 1
    return ans