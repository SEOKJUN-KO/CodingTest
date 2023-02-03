import sys
N = int(sys.stdin.readline())
count = [0]*(2*N+1)
zero = N
for _ in range(N):
    q =  int(sys.stdin.readline())
    count[N+q] += 1
for i in range(len(count)):
    if(count[i] != 0):
        for _ in range(count[i]):
            print(i-N)
