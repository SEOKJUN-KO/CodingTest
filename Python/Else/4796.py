import sys

n = 1
while(True):
    L, P, V = map(int, sys.stdin.readline().split());
    if(L == 0 and P == 0 and V == 0):
        break
    print("Case "+str(n)+": "+str(V//P*L+min(L, V%P)) )
    n += 1
