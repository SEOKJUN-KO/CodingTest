N, M = map(int, input().split() )
arr = list(map(int, input().split() ))
arr.sort()
isUsed = [False]*N
ans = []

def backtracking():
    global N, M
    if(len(ans) == M):
        print(" ".join(map(str, ans)))
    for i in range(N):
        if(not isUsed[i]):
            isUsed[i] = True
            ans.append(arr[i])
            backtracking()
            isUsed[i] = False
            ans.pop()

backtracking()
