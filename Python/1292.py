A, B = map(int, input().split())

st, ed, nxt = 1, 2, 2
ans = 0
f = 0
while(st<=B):
    if(A == B and st <= A < ed):
       ans += nxt-1
       break
    elif(st <= A <= B <= ed):
        ans += (B-A+1)*(nxt-1)
        break
    elif(st<= A < ed):
       ans += (ed-A)*(nxt-1)
       f = 1
    elif(st<= B < ed):
        ans += (B-st+1)*(nxt-1)
        break
    elif(f == 1):
        ans += (ed-st)*(nxt-1)
    st, ed = ed, ed+nxt
    nxt += 1
print(ans)
