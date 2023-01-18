N, M = map(int, input().split())

isUsed = [False]*(N+1)
arr = []
def backtracking(N, M):
    if(len(arr) == M):
        print(" ".join(map(str, arr)))
        return
    for i in range(1, N+1):
        if(not isUsed[i]):
            isUsed[i] = True
            arr.append(i)
            backtracking(N, M)
            isUsed[i] = False
            arr.pop()

backtracking(N, M)
