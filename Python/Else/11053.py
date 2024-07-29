N = int(input())
arr = list(map(int, input().split()))
DP = [1]
for i in range(1, len(arr)):
    m = 0
    for j in range(i-1, -1, -1):
        if(arr[j] < arr[i] and m < DP[j]):
            m = DP[j]
    DP.append(m+1)
print(max(DP))
