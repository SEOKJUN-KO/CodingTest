n = int(input())
DP = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


for i in range(n-1):
    BP = [0]*10
    for j in range(10):
        for k in range(j, 10):
            BP[j] += DP[k]%10007
    DP = BP[:]
print(sum(DP)%10007)
