import sys
import itertools

while(True):
    S = list(map(int, sys.stdin.readline().split()))
    if(S[0] == 0):
        exit()
    C = itertools.combinations(S[1:], 6)
    for c in C:
        print(" ".join(map(str, c)))
    print()
