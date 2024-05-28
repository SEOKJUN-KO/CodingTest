N, r, c = map(int, input().split())
i = 0
def recursion(sx, ex, sy, ey):
    global r, c, i
    if(ex-sx == 1):
        for y in range(sy, sy+2):
            for x in range(sx, sx+2):
                if(y == r and x == c):
                    print(i)
                    return
                i += 1
        return
    if( (sx+ex)//2 >= c and (sy+ey)//2 >= r): # 1
        recursion(sx, (sx+ex)//2, sy, (sy+ey)//2)
    elif( (sx+ex)//2 < c and (sy+ey)//2 >= r): # 2
        i += ((ex-sx+1)//2)**2
        recursion((sx+ex)//2+1, ex, sy, (sy+ey)//2)
    elif( (sx+ex)//2 >= c and (sy+ey)//2 < r): # 3
        i += ( ( (ex-sx+1)//2)**2 ) *2
        recursion(sx, (sx+ex)//2, (sy+ey)//2+1, ey)
    elif( (sx+ex)//2 < c and (sy+ey)//2 < r): # 4
        i += (((ex-sx+1)//2)**2)*3
        recursion((sx+ex)//2+1, ex, (sy+ey)//2+1, ey)
        
recursion(0, 2**N-1, 0, 2**N-1)
