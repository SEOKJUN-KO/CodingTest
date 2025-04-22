from collections import deque

def solution(land):
    ans = 0
    board = land
    que = deque()
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    dic = {}
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                board[y][x] = 0
                m = 1
                que.append([y, x])
                key = set([x])
                while(que):
                    ny, nx = que.popleft()
                    for i in range(4):
                        Y, X = ny+dy[i], nx+dx[i]
                        if 0 <= Y < len(board) and 0 <= X < len(board[0]) and board[Y][X] == 1:
                            key.add(X)
                            board[Y][X] = 0
                            m += 1
                            que.append([Y, X])
                for k in key:
                    if k not in dic.keys():
                        dic[k] = 0
                    dic[k] += m
    for key in dic.keys():
        if ans < dic[key]:
            ans = dic[key]
                
    return ans