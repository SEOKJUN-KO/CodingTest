N = int(input())

s, e = 1, 1
n = 6
ans = 1
while(True):
    if(s<=N<=e):
        print(ans)
        exit()
    s, e = e+1, e+n
    n, ans = n + 6, ans + 1
