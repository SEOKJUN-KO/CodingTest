import sys
input = sys.stdin.readline

def isPrime(n):
    for i in range(2, n):
        if(i*i > n):
            break
        if(n%i == 0):
            return 0
    return 1
n = int(input())
ans = 0
DP = [-1]*(123456*2+1)

while(n != 0):
    for i in range(n+1, 2*n+1):
        if(DP[i] == -1):
            DP[i] = isPrime(i)
        ans += DP[i]
    print(ans)
    ans = 0
    n = int(input())
