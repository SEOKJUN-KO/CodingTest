import sys

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append( list(map(int, sys.stdin.readline().split() )) )
    
arr = [0, 0, 0]
def recursion(sx, ex, sy, ey):
    if(sx == ex):
        return board[sy][sx]
    elif(sx > ex):
        return -2
    n = (ex-sx)//3
    A = recursion( sx,       sx+n,     sy,       sy+n )
    B = recursion( sx+n+1,   sx+2*n+1, sy,       sy+n )
    C = recursion( sx+2*n+2, ex,       sy,       sy+n )
    D = recursion( sx,       sx+n,     sy+n+1,   sy+2*n+1 )
    E = recursion( sx+n+1,   sx+2*n+1, sy+n+1,   sy+2*n+1 )
    F = recursion( sx+2*n+2, ex,       sy+n+1,   sy+2*n+1 )
    G = recursion( sx,       sx+n,     sy+2*n+2, ey )
    H = recursion( sx+n+1,   sx+2*n+1, sy+2*n+2, ey )
    I = recursion( sx+2*n+2, ex,       sy+2*n+2, ey )
    if(A==B==C==D==E==F==G==H==I):
        return A
    else:
        for i in [A, B, C, D, E, F, G, H, I]:
            if(i == -1):
                arr[0] += 1
            elif(i == 0):
                arr[1] += 1
            elif(i == 1):
                arr[2] += 1
        return -2
Q = recursion(0, N-1, 0, N-1)
if(Q == -1):
    arr[0] += 1
elif(Q == 0):
    arr[1] += 1
elif(Q == 1):
    arr[2] += 1
for a in arr:
    print(a)
