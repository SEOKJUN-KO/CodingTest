N = int(input())
D = [1, 2]

for i in range(2, N+1):
    D.append((D[i-1]+D[i-2])%10007)
print(D[N-1])