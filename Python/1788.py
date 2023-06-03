DP = [0, 1, 1]
n = int(input())
a = abs(n)
if( len(DP) < a ):
    for i in range(len(DP)-1, a):
        DP.append( (DP[i]+DP[i-1])%1000000000 )
if(n == 0):
    print(0)
    print(DP[n])
elif(n > 0):
    print(1)
    print(DP[n])
else:
    if(a%2 == 0):
        print(-1)
        print(DP[a])
    else:
        print(1)
        print(DP[a])
