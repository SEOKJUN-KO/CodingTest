def isPelindrom(n):
    s = str(n)
    st, ed = 0, len(s)-1
    while(st < ed):
        if(s[st] != s[ed]):
            return 0
        st += 1
        ed -= 1
    return 1

def isPrime(n):
    if(n == 1):
        return 0
    for i in range(2, n):
        if( i*i > n ):
            break
        if(n%i == 0):
            return 0
    return 1

n = int(input())
while(True):
    rPe = isPelindrom(n)
    if(rPe == 1):
        rPr = isPrime(n)
        if(rPr == 1):
            print(n)
            exit()
    n += 1
