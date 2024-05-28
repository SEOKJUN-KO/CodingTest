import sys

def sumN(st):
    s = 0
    for c in st:
        if(not c.isalpha()):
            s += int(c)
    return s

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().strip())
ans = sorted(arr, key = lambda x: (len(x), sumN(x), x))
for a in ans:
    print(a)
