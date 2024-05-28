N, S = map(int, input().split())
arr = list(map(int, input().split() ))

def backtracking(x, total):
    global S, N
    ans = 0
    if(x == N):
        if(total == S):
            return 1
        return 0
    ans += backtracking(x+1, total+arr[x])
    ans += backtracking(x+1, total)
    return ans
    
A = backtracking(0, 0)
if(S == 0 and A > 0):
    print(A-1)
else:
    print(A)
