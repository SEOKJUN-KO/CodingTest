N, M = map(int, input().split() )
arr = list(map(int, input().split() ))
arr.sort()
ans = []

def backtracking():
    global N, M
    if(len(ans) == M):
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
