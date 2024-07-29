import sys

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append( list(map(int, sys.stdin.readline().split() )) )
    
arr = [0, 0]
def recursion(sx, ex, sy, ey):
    if(sx == ex):
        return board[sy][sx]
    A = recursion(sx, (sx+ex)//2, sy, (sy+ey)//2 )
    B = recursion((sx+ex)//2+1, ex, sy, (sy+ey)//2)
    C = recursion(sx, (sx+ex)//2, (sy+ey)//2+1, ey)
    D = recursion((sx+ex)//2+1, ex, (sy+ey)//2+1, ey)
    if(A==B==C==D):
        return A
    else:
        for i in [A, B, C, D]:
            if(i != -1):
                arr[i] += 1
        return -1
F = recursion(0, N-1, 0, N-1)
if(F != -1):
    arr[F] += 1
for a in arr:
    print(a)
