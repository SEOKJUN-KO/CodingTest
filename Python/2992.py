n = int(input())
arr = list(str(n))
isUsed = [False]*(len(arr))
ans = float('inf')
joinA = []
def calculate(deep):
    global n, ans
    if(deep==len(arr)):
        if(joinA[0] == 0):
            return
        if( joinA != [] and n < int("".join(joinA)) and int("".join(joinA)) - n < ans ):
            ans = int("".join(joinA)) - n
            
        return
    for i in range(len(arr)):
        if(isUsed[i] == False):
            isUsed[i] = True
            joinA.append(arr[i])
            calculate(deep+1)
            joinA.pop()
            isUsed[i] = False

calculate(0)
if(ans == float('inf')):
    print(0)
else:
    print(ans+n)
