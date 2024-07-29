import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

s = 0

def isPrime(n):
    f = 0
    for i in range(2, n):
        if(i*i > n):
            break
        if(n%i == 0):
            f = 1
            break
    if(f == 0):
        return 1
    else:
        return 0
        
for a in arr:
    if(a == 1):
        continue
    s += isPrime(a)
print(s)
