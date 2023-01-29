N, M = map(int, input().split() )
arr = list(map(int, input().split() ))
arr.sort()
com = set([])
ans = []
isUsed = [False]*N

def backtracking():
    global N, M
    if(len(ans) == M):
        if(" ".join(map(str, ans)) not in com):
            com.add(" ".join(map(str, ans)))
            print(" ".join(map(str, ans)))
        return
    for i in range(N):
        if(not isUsed[i]):
            ans.append(arr[i])
            isUsed[i] = True
            backtracking()
            isUsed[i] = False
            ans.pop()

backtracking()
