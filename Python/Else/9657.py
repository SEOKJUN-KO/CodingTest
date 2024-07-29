N = int(input())
D = [0,1,2,1,1,1,1,2]

if(N>7):
    for i in range(8, N+1):
        A, B, C = D[i-1]+1, D[i-3]+1, D[i-4]+1
        if(A%2 == 1 or B%2 == 1 or C%2 == 1): D.append(1)
        else: D.append(2)

if(D[N]%2 == 1): print("SK")
else: print("CY")
