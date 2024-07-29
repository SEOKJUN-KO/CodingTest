import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    i = 2
    dic = {}
    cnt = 0
    while(i <= n):
        if(n%i == 0):
            n = n//i
            cnt += 1
        else:
            if(cnt != 0):
                dic[i] = cnt
            i += 1
            cnt = 0
    if(cnt != 0):
        dic[i] = cnt
    for k in dic.keys():
        print(k, dic[k])
