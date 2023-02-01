L, C = map(int, input().split())
arr = list(input().split())
arr = sorted(arr)
ans = []

def backtracking():
    global L, C
    if(len(ans) == L):
        s = 0
        for c in ['a', 'e', 'i', 'o', 'u']:
            if(c in ans):
                s += 1
        if(s > 0 and L - s > 1):
            print("".join(ans))
        return
    for i in range(C):
        if(ans == []):
            ans.append(arr[i])
            backtracking()
            ans.pop()
        elif(ans[-1] < arr[i]):
            ans.append(arr[i])
            backtracking()
            ans.pop()
backtracking()
