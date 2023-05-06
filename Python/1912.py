N = int(input())
arr = list(map(int, input().split()))

DP = [arr[0]]
for i in range(1, N):
    if(DP[i-1] < 0):
        DP.append(arr[i])
    else:
        DP.append(arr[i]+DP[i-1])
print(max(DP))
