N, M = map(int,input().split())

isUsed = [False]*(N+1)
arr = []
def backtracking():
    global N, M
    if(len(arr) == M):
        print(" ".join(map(str, arr)) )
        return
    for i in range(1, N+1):
        if(arr == []):
            isUsed[i] = True
            arr.append(i)
            backtracking()
            arr.pop()
            isUsed[i] = False
        elif(not isUsed[i] and arr[-1] < i):
            isUsed[i] = True
            arr.append(i)
            backtracking()
            arr.pop()
            isUsed[i] = False
backtracking()
