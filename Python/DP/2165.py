import sys
input = sys.stdin.readline

def Input():
    return int(input())

def DP(arr):
    if len(arr) == 1 or len(arr) == 2:
        return sum(arr)
    DP = [[0, arr[0], arr[0]], [arr[0], arr[1], arr[0]+arr[1]]]
    ans = max(max(DP[0]), max(DP[1]))
    for i in range(2, len(arr)):
        X = ans #이번에는 안 마심
        A = DP[i-1][0]+arr[i] # 연속 1잔 [이전 잔은 안 마심]
        B = DP[i-1][1]+arr[i] # 연속 2잔 [이전잔 마심]
        DP.append([X, A, B])
        if ans < A: ans = A
        if ans < B: ans = B
    print(DP)
    return ans

def main():
    N = Input()
    arr = []
    for _ in range(N):
        arr.append(Input())
    print(DP(arr))
main()