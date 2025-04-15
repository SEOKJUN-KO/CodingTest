from collections import deque

dd, dy, dx = ["u", "d", "r", "l"], [-1, 1, 0, 0], [0, 0, 1, -1]
def solution(board):
    ans = float('inf')
    que = deque()
    N = len(board)
    B = [ [ {"u": float('inf'), "d": float('inf'), "r": float('inf'), "l": float('inf')} for _ in range(N)] for _ in range(N)]
    if board[0][1] == 0:
        B[0][1]["r"] = 100
        que.append([0, 1, "r"])
    if board[1][0] == 0:
        B[1][0]["d"] = 100
        que.append([1, 0, "d"])
    while(que):
        y, x, d = que.popleft()
        for i in range(4):
            Y, X, D = y+dy[i], x+dx[i], dd[i]
            if 0 <= Y < N and 0 <= X < N and board[Y][X] != 1:
                if (d == "r" or d == "l") and (D == "u" or D == "d") and B[y][x][d] + 600 < B[Y][X][D]:
                    B[Y][X][D] = B[y][x][d] + 600
                    que.append([Y, X, D])
                elif (d == "u" or d == "d") and (D == "l" or D == "r") and B[y][x][d] + 600 < B[Y][X][D]:
                    B[Y][X][D] = B[y][x][d] + 600
                    que.append([Y, X, D])
                elif (d == D) and B[y][x][d] + 100 < B[Y][X][D]:
                    B[Y][X][D] = B[y][x][d] + 100
                    que.append([Y, X, D])
                if (Y == N-1 and X == N-1 and ans > B[Y][X][D]):
                    ans = B[Y][X][D]
    return ans