import sys
N = int(sys.stdin.readline())
board = []
for _ in range(N):
    arr = []
    st = sys.stdin.readline().strip()
    for c in st:
        arr.append(int(c))
    board.append(arr)

def recursion(sx, ex, sy, ey):
    if(sx == ex):
        return str(board[sy][sx])
    A = recursion(sx, (sx+ex)//2, sy, (sy+ey)//2 )
    B = recursion((sx+ex)//2+1, ex, sy, (sy+ey)//2)
    C = recursion(sx, (sx+ex)//2, (sy+ey)//2+1, ey)
    D = recursion((sx+ex)//2+1, ex, (sy+ey)//2+1, ey)
    if(A==B==C==D and len(A) == 1):
        return A
    else:
        st = "("
        for c in [A, B, C, D]:
            st += c
        st+=")"
        return st
print(recursion(0, N-1, 0, N-1))
