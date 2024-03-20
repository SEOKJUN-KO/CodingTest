def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
        

def solution(n, k):
    ans = 0
    n = n
    tmp = ""
    while(n > k):
        tmp += str(n%k)
        n = n//k
        if n < k: tmp += str(n)
    arr = []
    t = ""
    for c in tmp[::-1]:
        if c != "0":
            t += c
        else:
            if t != "":
                q = int(t)
                if q != 1:
                    arr.append(q)
            t = ""
    if t != "":
        q = int(t)
        if q != 1:
            arr.append(q)
    for a in arr:
        if isPrime(a): ans += 1
        
    return ans
