A, N, M = map(int, input().split())

def Func(A, N, M):
    if(N == 1):
        return A%M
    val = Func(A, N//2, M)
    val = val*val%M
    if(N%2 == 0):
        return val
    return val*A%M

print(Func(A, N, M))
