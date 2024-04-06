# 높이 차이 2 이상 불가능

def isThisPossible(arr, X):
    idxArr = []
    dArr = []
    for i in range(N-1):
        if abs(arr[i] - arr[i+1]) >= 2: return False
        if arr[i] > arr[i+1]:
            idxArr.append(i+1)
            dArr.append(1)
        elif arr[i] < arr[i+1]:
            idxArr.append(i)
            dArr.append(-1)
    if idxArr == []: return True
    checkArr = [ False for _ in range(len(arr)) ]
    for i in range(0, len(idxArr)):
        idx = idxArr[i]
        if dArr[i] < 0:
            if idx -X + 1 < 0: return False
            for j in range(idx-X+1, idx+1):
                if checkArr[j]: return False
                checkArr[j] = True
        else:
            if idx+X > len(arr) : return False
            for j in range(idx, idx+X):
                if checkArr[j]: return False
                checkArr[j] = True
    return True

T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().strip().split(" "))
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip().split(" "))))
    xTmp = [ [] for _ in range(N) ]
    ans = 0
    for y in range(N):
        if isThisPossible(board[y], X): ans += 1
        for x in range(N):
            xTmp[x].append(board[y][x])
    for tmp in xTmp:
        if isThisPossible(tmp, X): ans += 1
    print("#%d %d" % (test_case, ans))
