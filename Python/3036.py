N = int(input())
arr = list(map(int, input().split() ))
def findN(a, b):
    i = 2
    r = 1
    while(i <= a and i <= b):
        if(a%i == 0 and b%i == 0):
            r *= i
            a = a//i
            b = b//i
        else:
            i += 1
    return r

for i in range(1, N):
    r = findN(arr[0], arr[i])
    print("%d/%d" %(arr[0]//r, arr[i]//r))
