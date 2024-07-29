import sys
input = sys.stdin.readline
N = int(input())
if(N == 1):
    print(0)
    exit()
steps = []
for _ in range(N-1):
    steps.append(list(map(int, input().split())))
K = int(input())

DP = [[0, 0], [steps[0][0], steps[0][0]]]
for now in range(1, len(steps)):
    f = min(DP[now]) + steps[now][0]
    s = min(DP[now-1]) + steps[now-1][1]
    DP.append([f, s])
if(N >= 4): # len(DP) == N
    ans = min(DP[-1])
    for i in range(3, N):
        Q = min(DP[i-3])+K
        if(Q > min(DP[i])):
            continue
        tmpDP = DP[:]
        tmpDP[i] = [Q, Q]
        for j in range(i, N-1):
            f = min(tmpDP[j]) + steps[j][0]
            s = min(tmpDP[j-1]) + steps[j-1][1]
            tmpDP[j+1] = [f,s]
        ans = min(ans, min(tmpDP[-1]))
    print(ans)
else:
    print(min(DP[-1]))
