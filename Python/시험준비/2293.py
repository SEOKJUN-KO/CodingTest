import sys
input = sys.stdin.readline

coins = []
def makeCoins(N):
    global coins
    for _ in range(N):
        coins.append(int(input()))
    coins = sorted(coins)

def dp(K):
    global coins
    arr = [ 0 for _ in range(K+1) ]
    arr[0] = 1
    idx = coins[0]
    while(idx <= K):
        arr[idx] = 1
        idx += coins[0]
    for coin in coins[1:]:
        for i in range(coin, K+1):
            arr[i] += arr[i-coin]
    print(arr[-1])

def solution():
    N, K = map(int, input().strip().split(" "))
    makeCoins(N)
    dp(K)
solution()