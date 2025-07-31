N = int(input())
# [이전 위치, 횟수]
DP = [0, 0]
exArr = [0, 0]

for i in range(2, N+1):
    tmp = 9999999999
    ex = -1
    if i%3 == 0:
        tmp = DP[i//3]
        ex = i//3
    if i%2 == 0 and tmp > DP[i//2]:
        tmp = DP[i//2]
        ex = i//2
    if tmp > DP[i-1]:
        tmp = DP[i-1]
        ex = i-1
    tmp += 1
    
    DP.append(tmp)
    exArr.append(ex)
print(DP[-1])
answer = [N]
while(N > 1):
    answer.append(exArr[N])
    N = exArr[N]
print(" ".join(map(str,answer)))