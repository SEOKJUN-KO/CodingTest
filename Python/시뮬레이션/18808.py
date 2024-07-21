import sys
input = sys.stdin.readline

N, M, K = map(int, input().split(" "))

board = []
for _ in range(N):
    board.append([0]*(M))
    
def turn(arr, R, C):
    sticker = []
    for x in range(C):
        tmp = []
        for y in range(R-1, -1, -1):
            tmp.append(arr[y][x])
        sticker.append(tmp)
    return sticker
    
for _ in range(K):
    sticker = []
    R, C = map(int, input().split(" "))
    for _ in range(R):
        sticker.append(list(map(int, input().split(" "))))
    for i in range(4):
        if ( (N < R) or (M < C)):
            arr = turn(sticker, R, C)
            sticker = arr
            (R, C) = (C, R)
            continue
        flag = False
        cnt, T = 0, R*C
        saveY, saveX = 0, 0
        nY, nX = 0, 0
        while(not flag and saveY+R <= N and saveX+C <= M):
            if (board[nY][nX]*sticker[cnt//C][cnt%C] == 0):
                cnt += 1
                nX += 1
                if nX == saveX+C:
                    nX = saveX
                    nY += 1
            else:
                cnt = 0
                saveX += 1
                if saveX+C > M:
                    saveX = 0
                    saveY += 1
                nY, nX = saveY, saveX
            if cnt == T:
                for y in range(saveY, saveY+R):
                    for x in range(saveX, saveX+C):
                        if sticker[y-saveY][x-saveX] == 1:
                            board[y][x] = 1
                flag = True
        if flag: break
        arr = turn(sticker, R, C)
        sticker = arr
        (R, C) = (C, R)
ans = 0
for y in range(N):
    ans += sum(board[y])
print(ans)
    
