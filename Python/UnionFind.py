import sys
input = sys.stdin.readline

P = [i for i in range(10)]

def findParent(x):
    if( P[x] == x ): return x
    return findParent(P[x])

def unionParent(x, y):
    X = findParent(x)
    Y = findParent(y)
    if(X<=Y):
        P[Y] = P[X]
        return
    else:
        P[X] = P[Y]

def checkSame(x, y):
    X = findParent(x)
    Y = findParent(y)
    if(X==Y): return 1
    else: return 0

unionParent(1, 2)
unionParent(2, 3)
unionParent(1, 4)

unionParent(5, 6)
unionParent(7, 8)
unionParent(5, 7)

print(checkSame(1, 5))    
