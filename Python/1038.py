n = int(input())

if(n >= 1023):
    print(-1)
    exit()
isUsed = [False]*(10)

cnt = -1
ans = []
def caculate(length, deep):
    global cnt, n
    if(deep > length):
        cnt += 1
        if(cnt == n):
            print("".join(map(str,ans)))
            exit()
        return
    for i in range(10):
        if(isUsed[i] == False):
            if(ans == []):
                isUsed[i] = True
                ans.append(i)
                caculate(length, deep+1)
                ans.pop()
                isUsed[i] = False
            elif(ans[-1] > i):
                isUsed[i] = True
                ans.append(i)
                caculate(length, deep+1)
                ans.pop()
                isUsed[i] = False
for l in range(10):
    caculate(l, 0)
