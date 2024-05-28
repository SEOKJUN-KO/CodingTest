n = int(input())

DP = [1, 1, 1]
for i in range(2, n+1):
    BP = [0, 0, 0]
    BP[0] += (DP[1]+DP[2])%9901
    BP[1] += (DP[0]+DP[2])%9901
    BP[2] += (DP[0]+DP[1]+DP[2])%9901
    DP = BP
print(sum(DP)%9901)
