N = int( input() )
if(N == 1):
    exit()
n = N
i = 2
while(i <= N):
    if(n%i == 0):
        n //= i
        print(i)
    else:
        i += 1
