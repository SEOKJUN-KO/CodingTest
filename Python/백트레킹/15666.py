N, M = map(int, input().split() )
arr = list(map(int, input().split() ))
arr = set(arr)
arr = list(arr)
arr.sort()
N = len(arr)
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
        if(ans == []):
            ans.append(arr[i])
            backtracking()
            ans.pop()
        elif(ans[-1] <= arr[i]):
            ans.append(arr[i])
            backtracking()
            ans.pop()
backtracking()
