def isPrime(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

arr = []
dic = {}
ans = 0
sumed = 0

def allCase(level, idx):
    global arr, sumed, ans
    if (level == 3):
        if sumed not in dic.keys():
            if isPrime(sumed):
                ans += 1
                dic[sumed] = 1
            else:
                dic[sumed] = 0
        else:
            ans += dic[sumed]
        return
    
    for i in range(idx+1, len(arr)):
        sumed += arr[i]
        allCase(level+1, i)
        sumed -= arr[i]
    return

def solution(nums):
    global arr, ans
    arr = sorted(nums)
    allCase(0, -1)
    return ans
