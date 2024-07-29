N = int(input())

arr = []

def isPrime(num):
    if(num == 1): return False
    for i in range(2, num):
        if(i*i > num):
            return True
        if(num%i == 0):
            return False
    return True

def backT():
    global N
    if( len(arr) == N):
       print("".join(arr)) 
       return
    for i in range(1, 10):
        arr.append(str(i))
        if( isPrime( int( "".join(arr) ) )  ):
            backT()
        arr.pop()

backT()
