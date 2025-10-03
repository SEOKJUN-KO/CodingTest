answer = 'impossible'
LY, LX = 0, 0

def printBoard(y, x, LY, LX, tY, tX):
    for ny in range(LY):
        tmp = ''
        for nx in range(LX):
            if ny == y and nx == x:
                tmp+='S'
            elif ny == tY and nx == tX:
                tmp+='E'
            else:
                tmp+='.'
        print(tmp)
            
def calculate(y, x, tY, tX, k):
    if ( k - (abs(tY-y)+abs(tX-x)) ) % 2 == 1: return
    
    global answer, LY, LX, target
    tmp = ''
    A = (LY-1-y) # d
    minA = max(tY-y, 0)
    B = x # l
    minB = max(x-tX, 0)
    C = 0 # rl
    D = tX # r
    E = (LY-1-tY) # u
    
    if (A+B+C+D+E < k):
        C = ( k - (A+B+D+E) ) // 2
        answer = 'd'*A+'l'*B+'rl'*C+'r'*D+'u'*E
    elif (A+B+C+D+E == k):
        answer = 'd'*A+'l'*B+'r'*D+'u'*E
    else:
        while(B > minB):
            B -= 1
            D -= 1
            if k == (A+B+D+E):
                answer = 'd'*A+'l'*B+'r'*D+'u'*E
                return
        while(A > minA):
            A -= 1
            E -= 1
            if k == (A+B+D+E):
                answer = 'd'*A+'l'*B+'r'*D+'u'*E
                return
        if k == (A+B+D+E):
            answer = 'd'*A+'l'*B+'r'*D+'u'*E
            return
def solution(n, m, x, y, r, c, k):
    global answer, LY, LX
    LY = n
    LX = m
    # printBoard(x-1, y-1, LY, LX, r-1, c-1)
    calculate(x-1, y-1, r-1, c-1, k)
    return answer