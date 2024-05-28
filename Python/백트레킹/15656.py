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
        ans.append(arr[i])
        backtracking()
        ans.pop()

backtracking()
