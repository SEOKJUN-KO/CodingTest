E, S, M = map( int, input().split() )
ans = 1

while(E+S+M != 3):
    m = max(E, S, M)-1
    E = E-m
    while(E<=0):
        E += 15
    S = S-m
    while(S<=0):
        S += 28
    M = M-m
    while(M<=0):
        M += 19
    ans += m
print(ans)
