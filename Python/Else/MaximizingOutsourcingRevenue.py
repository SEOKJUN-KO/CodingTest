# https://www.codetree.ai/training-field/frequent-problems/problems/max-of-outsourcing-profit/description?page=1&pageSize=20&tier=5%2C10
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    time, money = map(int, input().split())
    arr.append([i, i+time, money])
DP = [0]*(len(arr))
if(arr[0][1] <= n):
	DP[0] = arr[0][2]
for i in range(1, len(arr)):
    if(arr[i][1] > n): 
        continue
    tmp = 0
    for j in range(i-1, -1, -1):
        if(arr[j][1] <= arr[i][0] and tmp < DP[j]):
            tmp = DP[j]
    DP[i] = tmp + arr[i][2]
print(max(DP))
