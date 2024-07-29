import sys
input = sys.stdin.readline
arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))

if( n < 3 ):
    print(sum(arr))
    exit()
DP = arr[:3]
for i in range(3, n):
    DP.append( min(DP[i-1], DP[i-2], DP[i-3])+arr[i])
print(sum(arr)-min(DP[n-3:]))
