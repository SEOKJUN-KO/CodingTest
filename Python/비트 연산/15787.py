import sys
input= sys.stdin.readline

def first(arr, i , x):
    arr[i] |= (1<<((21-x)-1))

def second(arr, i, x):
    arr[i] ^= (1<<((21-x)-1))

def third(arr, i):
    arr[i] = (arr[i] >> 1)

def fourth(arr, i):
    arr[i] = (arr[i] << 1)
    C = 0xfffff
    arr[i] &= C

def doOrder(arr, M):
    for _ in range(M):
        O = list(map(int, input().split(" ")))
        if O[0] == 1:
            first(arr, O[1]-1, O[2])
        elif O[0] == 2:
            second(arr, O[1]-1, O[2])
        elif O[0] == 3:
            third(arr, O[1]-1)
        else:
            fourth(arr, O[1]-1)

def main():
    N, M = map(int, input().split(" "))
    arr = [ 0 for _ in range(N) ]
    doOrder(arr, M)
        
    s = set(arr)
    print(len(s))

main()