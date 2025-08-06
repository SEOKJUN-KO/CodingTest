import sys
input = sys.stdin.readline

def getCoins(N):
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    return coins

def DP(K, coins):
    D = [ 0 for _ in range(K+1) ]
    D[0] = 1
    
    for coin in coins:
        if coin < K:
            D[coin] += 1
        for i in range(coin+1, K+1):
            D[i] += D[i-coin]
    return D

def main():
    N, K = map(int, input().split(" "))
    coins = getCoins(N)
    D = DP(K, coins)
    print(D[-1])
main()