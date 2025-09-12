import sys
input = sys.stdin.readline

# 1. 밀가루 양이 가장 작은 위치 + 1 [ 최소 값 모두에게 ]
# 2. 도우 말기
# 3. 도우 누르기
# 4. 도우 두번 반으로 접기
# 5. 도우 누르기


flours = []

def makeflours(n):
    global flours
    arr = list(map(int, input().strip().split(" ")))
    for _ in range(n//2):
        flours.append( [ 0 for _ in range(n) ])
    flours[0] = arr

# 1. 로직 O, 최적화 X
def addFlour(n): # 100
    global flours
    minN = min(flours[0])
    for i in range(n):
        if flours[0][i] == minN:
            flours[0][i] += 1

# 2. 로직 O, 최적화 X
def roll(n):
    global flours
    h = 1
    w = 1
    mode = 0
    
    while(h <= n-h*w):
        tmp = [ [ 0 for _ in range(n) ] for _ in range(n//2 + 1) ]
        Y = 0
        for x in range(w-1, -1, -1):
            Y += 1
            for y in range(h):
                tmp[Y][y] = flours[y][x]
        
        X = 0    
        for x in flours[0][w:]:
            tmp[0][X] = x
            X += 1
        
        flours[:] = tmp

        if mode == 0: h += 1
        else: w += 1
        mode = (mode+1)%2
    return h

# 3. 로직 O
def press(h, n):
    global flours
    tmp = [ [0 for _ in range(n)] for _ in range(h) ]
    # 한번에 계산하기
    for y in range(h):
        for x in range(n):
            if flours[y][x] == 0: break
            for dy, dx in [ [1, 0], [0, 1]]:
                Y, X = y+dy, x+dx
                if ( 0 <= Y < h and 0 <= X < n and flours[Y][X] != 0 ):
                    A = abs(flours[y][x] - flours[Y][X]) // 5
                    if flours[y][x] > flours[Y][X]:
                        tmp[y][x] -= A
                        tmp[Y][X] += A
                    else:
                        tmp[y][x] += A
                        tmp[Y][X] -= A
    # 계산하기
    for y in range(h):
        for x in range(n):
            if flours[y][x] == 0: break
            flours[y][x] += tmp[y][x]
    # 한줄로 만들기
    tmp = [ [ 0 for _ in range(n) ] for _ in range(n//2 + 1) ]
    idx = 0
    
    for x in range(n):
        for y in range(h):
            if flours[y][x] == 0: break
            tmp[0][idx] = flours[y][x]
            idx += 1
    flours[:] = tmp

# 4. 로직 O, 최적화 X
def fold(n):
    global flours
    
    h = 1
    w = n//2
    cnt = 1
    while(cnt <= 2):
        tmp = [ [ 0 for _ in range(n) ] for _ in range(4) ]

        for x in range(w-1, -1, -1):
            for y in range(h-1, -1, -1):
                if h == 1:
                    tmp[h-y][w-x-1] = flours[y][x]
                else:
                    tmp[h+1-y][w-x-1] = flours[y][x]
        
        for y in range(h):
            for x in range(w):
                tmp[y][x] = flours[y][x+w]

        w = w//2
        h = 2
        flours[:] = tmp
        cnt += 1

def main():
    global flours
    n, k = map(int, input().strip().split(" "))
    answer = 0
    makeflours(n)
    while( max(flours[0]) - min(flours[0]) > k):
        addFlour(n)
        h = roll(n)
        press(h, n)
        fold(n)
        press(4, n)
        answer += 1
    print(answer)
    
main()