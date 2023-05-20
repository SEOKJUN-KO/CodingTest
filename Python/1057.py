n, a, b = map(int, input().split() )

ans = 0
while(a!=b):
    ans += 1
    if(a%2 == 1):
        a = a//2 + 1
    else:
        a = a//2
    if(b%2 == 1):
        b = b//2 + 1
    else:
        b = b//2
print(ans)
