import sys
input = sys.stdin.readline

bags = []
def makeBags(N):
    global bags
    for _ in range(N):
        W, V = map(int, input().split(" "))
        bags.append([W, V])
    bags = sorted(bags, key=lambda x: x[0])

def dp(K):
    global bags
    arr = [ 0 for _ in range(K+1) ]
    
    for W, V in bags:
        for i in range(K, W-1, -1):
            arr[i] = max(arr[i], arr[i-W]+V)
    print(arr[-1])


def solution():
    global bags
    N, K = map(int, input().split(" "))
    makeBags(N)
    dp(K)
solution()