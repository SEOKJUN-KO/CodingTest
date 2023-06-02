N = input()

DP = [1, 1, 2] #0, 1, 2

def makeDP(cnt):
    if( cnt+1 > len(DP) ):
        for j in range(len(DP), cnt+1):
            DP.append( (DP[j-1]+DP[j-2])%1000000 )

cnt = 1
ans = 1
if(N[0] == '0'):
    print(0)
    exit()
for i in range(len(N)-1):
    if(N[i]+N[i+1] == "00" ):
        print(0)
        exit()
    if(N[i] == "0"):
        continue
    if( 1 <= int(N[i]+N[i+1]) <= 26):
        if(int(N[i]+N[i+1])%10 == 0):
            cnt -= 1
            makeDP(cnt)
            ans = (ans*DP[cnt])%1000000
            cnt = 1
        else:
            cnt += 1
    else:
        if(int(N[i]+N[i+1])%10 == 0):
            print(0)
            exit()
        makeDP(cnt)
        ans = (ans*DP[cnt])%1000000
        cnt = 1
makeDP(cnt)
ans = (ans*DP[cnt])%1000000
print(ans)
