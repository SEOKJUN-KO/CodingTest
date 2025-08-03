import sys
#board = 4*10^2
input = sys.stdin.readline

def makeBoard(R):
    board = []
    for _ in range(R):
        board.append(list(input().strip()))
    return board

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
s = set()
ans = 0
def backTracking(board, R, C, ny, nx):
    global dy, dx, ans
    for i in range(4):
        Y, X = ny+dy[i], nx+dx[i]
        if 0 <= Y < R and 0 <= X < C and board[Y][X] not in s:
            s.add(board[Y][X])
            backTracking(board, R, C, Y, X)
            s.remove(board[Y][X])
    if ans < len(s):
        ans = len(s)


def main():
    global ans, s
    R, C = map(int, input().split(" "))
    board = makeBoard(R)
    s.add(board[0][0])
    backTracking(board, R, C, 0, 0)    
    print(ans)
main()