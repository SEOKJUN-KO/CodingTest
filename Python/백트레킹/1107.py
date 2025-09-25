ans = float('inf')

def backtracking(level, N, s, limit, now):
    global ans
    if level > limit+1:
        return
    for i in range(10):
        if i not in s:
            now = now*10
            now += i
            C = abs(N-now)+level
            if C < ans: ans = C
            backtracking(level+1, N, s, limit, now)
            now = now//10


def main():
    global ans
    N = int(input())
    M = int(input())
    if M == 0:
        A = len(str(N))
        B = abs(N-100)
        if A > B: print(B) 
        else: print(A)
        return
    arr = list(map(int, input().split(" ")))
    s = set()
    if M == 10:
        if N >= 100: print(N - 100)
        else: print(100 - N)
        return
    if N == 100:
        print(0)
        return
    ans = abs(N - 100)
    for a in arr: s.add(a)
    backtracking(1, N, s, len(str(N)), 0)
    print(ans)
main()