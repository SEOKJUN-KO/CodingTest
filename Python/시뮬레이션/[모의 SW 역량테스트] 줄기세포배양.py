dx, dy = [+1, -1, +0, +0], [+0, +0, +1, -1]

T = int(input().strip())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().strip().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip().split())))
    dic = {}
    usedP = set([])
    for y in range(N):
        for x in range(M):
            if board[y][x] != 0:
                dic[board[y][x]] = dic.get(board[y][x], [])
                dic[board[y][x]].append([y,x,board[y][x]])
                usedP.add(str(y)+"."+str(x))
    liveDic = {}
    for k in range(K):
        keyArr = list(dic.keys())
        keyArr.sort(reverse=True)
        tmpDic = {}

        lKeyArr = list(liveDic.keys())
        lKeyArr.sort(reverse=True)
        if lKeyArr != []:
            for i in range(len(lKeyArr)):
                tmpDic[lKeyArr[i]-1] = liveDic[lKeyArr[i]]
        if 0 in tmpDic.keys(): del(tmpDic[0])
        liveDic = tmpDic.copy()

        tmpDic = {}
        for i in range(len(keyArr)):
            tmpDic[keyArr[i]-1] = dic[keyArr[i]]
        if -1 in tmpDic.keys():
            tmpDic[-1].sort(key = lambda x: -x[2])
            for y, x, w in tmpDic[-1]:
                tmpDic[w] = tmpDic.get(w, [])
                if w != 1: liveDic[w - 1] = liveDic.get(w - 1, 0) + 1
                for j in range(4):
                    Y, X = y+dy[j], x+dx[j]
                    if str(Y)+"."+str(X) not in usedP:
                        tmpDic[w].append([Y,X,w])
                        usedP.add(str(Y)+"."+str(X))
            del(tmpDic[-1])
        dic = tmpDic.copy()
    cnt = 0
    for key in dic.keys():
        cnt += len(dic[key])
    for key in liveDic.keys():
        cnt += liveDic[key]
    print("#%d %d" % (test_case, cnt))






