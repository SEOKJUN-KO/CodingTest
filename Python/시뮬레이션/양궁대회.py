# 라이언이 #가장 큰 점수# 차이로 어피치를 이겨야 한다
answer = [0, [-1]]
arr = []
comp = []

def findSmall():
    global arr, answer
    
    for i in range(10, -1, -1):
        if answer[1][i] == 0 and arr[i] == 0: continue
        if answer[1][i] < arr[i]:
            answer[1][:] = arr
        elif answer[1][i] == arr[i]: continue
        return
        
def calculate():
    global arr, answer
    lion, peach = 0, 0
    for i in range(11):
        a = arr[i]
        c = comp[i]
        if c < a:
            lion += 10 - i
        elif c >= a and c != 0: 
            peach += 10 - i
    if lion > peach and answer[0] <= lion - peach:
        score = lion - peach
        if answer[0] < score:
            answer[0] = score
            answer[1][:] = arr
            return
        findSmall()
        
def backtracking(n, s):
    global arr
    if len(arr) >= 11:
        if s == n:
            calculate()
        return
    for i in range(n+1):
        if s + i <= n:
            arr.append(i)
            s = s+i
            backtracking(n, s)
            s = s-i
            arr.pop()

def solution(n, info):
    global comp, answer
    comp[:] = info
    backtracking(n, 0)
    return answer[1]