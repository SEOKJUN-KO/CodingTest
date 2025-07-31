import sys
input = sys.stdin.readline

def makeBoard(N):
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split(" "))))
    return board

def calculate(D):
    for i in range(1, len(D)):
        for j in range(3):
            tmp = float('inf')
            for k in range(3):
                if j != k and tmp > D[i-1][k]:
                    tmp = D[i-1][k]
            D[i][j] += tmp
    return min(D[-1])

def main():
    N = int(input())
    D = makeBoard(N)
    print(calculate(D))
main()
