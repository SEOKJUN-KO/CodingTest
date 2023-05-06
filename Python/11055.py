N = int(input())
arr = list(map(int, input().split() ))
# print(arr)
DP = [arr[0]]
ans = 0
for i in range(1, len(arr)):
    k = 0
    for j in range(i-1, -1, -1):
        if( arr[j] < arr[i] ):
            if(k < DP[j] ):
                k = DP[j]
    DP.append(k+arr[i])
print(max(DP))
