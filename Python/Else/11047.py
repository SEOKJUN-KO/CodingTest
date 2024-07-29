import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)

s = 0
k = K
while(True):
    for a in arr[::-1]:
        s += k//a
        k = k%a
        if(k == 0):
            print(s)
            exit()
    k = K
    arr.pop()
