# M명 참가 # N*N 격자 미로 # start (1, 1)

### 참가자
# 모든 참가자 동시에 움직임
# 1초마다 상하좌우로 한 칸씩 움직임
# 최단거리: abs(x1-x2) + abs(y1-y2)
# 출구까지 최단거리가 가까워지는 방향[상, 하 우선]으로
# 칸 중복 가능
# 움직일 수 없는 상황은 안 움직임

### 미로
# 빈칸 - 이동 가능
# 벽 : 1 - 9 내구도 => 0 되면 빈칸
# 출구 : 도달 즉시 탈출
# 참가자가 모두 움직인 후, 회전
# 회전 정사각형 90도 회전: 한명 이상의 참가자와 출구를 포함한 가장 작은
# y 작은 것, c 작은 것 우선
# 회전된 벽 내구도 1 깎
# K초 반복

 # M명 참가 # N*N 격자 미로 # start (1, 1)

### 참가자
# 모든 참가자 동시에 움직임
# 1초마다 상하좌우로 한 칸씩 움직임
# 최단거리: abs(x1-x2) + abs(y1-y2)
# 출구까지 최단거리가 가까워지는 방향[상, 하 우선]으로
# 칸 중복 가능
# 움직일 수 없는 상황은 안 움직임

### 미로
# 빈칸 - 이동 가능
# 벽 : 1 - 9 내구도 => 0 되면 빈칸
# 출구 : 도달 즉시 탈출
# 참가자가 모두 움직인 후, 회전
# 회전 정사각형 90도 회전: 한명 이상의 참가자와 출구를 포함한 가장 작은
# 회전된 벽 내구도 1 깎
# K초 반복

dy, dx = [-1, +1, +0, +0], [+0, +0, -1, +1]
def moveToGate():
    global humanPosition, gatePosition, N, board, cnt
    tmpBoard = []
    for y in range(len(board)):
        tmpArr = []
        for x in range(len(board)):
            if board[y][x] > 0: tmpArr.append(board[y][x])
            elif board[y][x] == -999999999: tmpArr.append(-999999999)
            else: tmpArr.append(0)
        tmpBoard.append(tmpArr)
    for j in range(len(humanPosition)):
        position = humanPosition[j]
        minL = abs(position[0]-gatePosition[0]) + abs(position[1]-gatePosition[1])
        saveY, saveX = -1, -1
        y, x = position[0], position[1]
        for i in range(4):
            Y, X = y+dy[i], x+dx[i]
            if 0 <= Y < N and 0 <= X < N and board[Y][X] <= 0:
                resultL = abs(Y-gatePosition[0]) + abs(X-gatePosition[1])
                if minL > resultL:
                    minL = resultL
                    saveY, saveX = Y, X
        if saveY != -1:
            if [saveY, saveX] == gatePosition:
                cnt += abs(board[y][x])
            else:
                tmpBoard[saveY][saveX] += board[y][x]
                cnt += abs(board[y][x])
        else:
            tmpBoard[y][x] += board[y][x]
    board = tmpBoard.copy()
    humanPosition = []
    for y in range(len(board)):
        for x in range(len(board)):
            if -999999999 < board[y][x] <= -1: humanPosition.append([y, x])
    if len(humanPosition) == 0: return True
    return False
def rectangle():
    # 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
    global humanPosition, gatePosition, N, board
    minRectangleL = float('inf')
    saveY, saveX = -1, -1
    for l in range(1, len(board)+1):
        for y in range(len(board)-l):
            for x in range(len(board)-l):
                if y <= gatePosition[0] <= y+l and x <= gatePosition[1] <= x+l:
                    for humanY, humanX in humanPosition:
                        if y <= humanY <= y+l and x <= humanX <= x+l:
                            minRectangleL = l+1
                            saveY, saveX = y, x
                            break
                if saveY != -1: break
            if saveY != -1: break
        if saveY != -1: break

    topY, bottomY = saveY, saveY+minRectangleL-1
    leftX, rightX = saveX, saveX+minRectangleL-1
    arr = []
    for y in range(topY, bottomY+1):
        tmp = []
        for x in range(leftX, rightX+1):
            tmp.append(board[y][x])
        arr.append(tmp)
    tmp = [[0]*minRectangleL for _ in range(minRectangleL)]
    for y in range(minRectangleL):
        for x in range(minRectangleL):
            if arr[y][x] > 0: tmp[x][minRectangleL-1-y] = arr[y][x] -1
            else: tmp[x][minRectangleL-1-y] = arr[y][x]
    arr = tmp
    humanPosition = []
    for y in range(topY, bottomY+1):
        for x in range(leftX, rightX+1):
            board[y][x] = arr[y-topY][x-leftX]
    for y in range(len(board)):
        for x in range(len(board)):
            if -999999999 < board[y][x] <= -1: humanPosition.append([y, x])
            if board[y][x] == -999999999: gatePosition = [y, x]
    if len(humanPosition) > 0: return False
    return True

N, M, K = map(int, input().strip().split(" "))
board = []
humanPosition = []
gatePosition = []
cnt = 0
for _ in range(N):
    board.append(list(map(int, input().strip().split(" "))))
for _ in range(M):
    y, x = map(int, input().strip().split(" "))
    board[y-1][x-1] = -1
    humanPosition.append([y-1, x-1])
y, x = map(int, input().strip().split(" "))
board[y-1][x-1] = -999999999
gatePosition = [y-1, x-1]
for i in range(K):
    if moveToGate(): break
    if rectangle(): break
gatePosition[0], gatePosition[1] = gatePosition[0]+1, gatePosition[1]+1
print(cnt)
print(" ".join(map(str, gatePosition)))
