import sys
input = sys.stdin.readline

N = int(input())
if N == 1: print(0)
else:
    isPrime = [True]*(N+1)
    
    for i in range(2, min( int(N**(1/2))+3, N)):
        if not isPrime[i]: continue
        tmp = 2
        while(i*tmp<=N):
            isPrime[i*tmp] = False
            tmp += 1
    prime = []
    for i in range(2, N+1):
        if isPrime[i]: prime.append(i)
    ans = 0
    left, right, cnt = 0, 0, prime[0]
    while( left <= right ):
        if cnt > N:
            cnt -= prime[left]
            left += 1
        elif cnt <= N:
            if cnt == N: ans += 1
            right += 1
            if right == len(prime): break
            cnt += prime[right]
    print(ans)
