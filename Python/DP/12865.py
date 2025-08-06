import sys
input = sys.stdin.readline

def getThings(N):
    things = []
    for _ in range(N):
        w, v = map(int, input().split(" "))
        things.append([w, v])
    things = sorted(things, key=lambda x: x[0])
    return things

def DP(things, K):
    D = [[0 for _ in range(K+1)]]
    wage = 0
    idx = 1
    for w, v in things:
        D.append([ 0 for _ in range(K+1)])
        for i in range(min(w, K+1)):
            D[idx][i] = D[idx-1][i]
        
        for j in range(w, min(w+wage, K+1)):
            D[idx][j] = max(D[idx-1][j-w]+v, D[idx-1][j])
            
        for k in range(w+wage, K+1):
            D[idx][k] = D[idx-1][k]+v
        wage += w
        idx += 1
    return D

def main():
    N, K = map(int, input().split(" "))
    things = getThings(N)
    D = DP(things, K)
    print(D[-1][-1])
main()