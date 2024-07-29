N, M = map(int,input().split())

arr = []
def backtracking():
    global N, M
    if(len(arr) == M):
        print(" ".join(map(str, arr)) )
        return
    for i in range(1, N+1):
        if(arr == []):
            arr.append(i)
            backtracking()
            arr.pop()
        elif(arr[-1] <= i):
            arr.append(i)
            backtracking()
            arr.pop()
backtracking()
