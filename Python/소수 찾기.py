L = 0
number = ""
use = []
tmp = []
ans = set([])
def isPrime(n):
    if n <= 1: return False
    for i in range(2, n//2+1):
        if n%i == 0: return False
    return True
    

def backTracking():
    global number, L, use, tmp
    if len(tmp) == L:
        k = int("".join(tmp))
        if k not in ans:
            if isPrime(k):
                ans.add(k)
        return
    for i in range(len(number)):
        if not use[i]:
            use[i] = True
            tmp.append(number[i])
            backTracking()
            use[i] = False
            tmp.pop()
    return
    
def solution(numbers):
    global number, L, use, ans
    number = list(numbers)
    use = [False]*len(number)
    for i in range(1, len(number)+1):
        L = i
        backTracking()
    return len(ans)
