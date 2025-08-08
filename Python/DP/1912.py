import sys
input = sys.stdin.readline

def DP(arr):
    for i in range(1, len(arr)): #10^5
        arr[i] += arr[i-1]

def calculate(arr):
    print(arr)
    ans = arr[0]
    m = arr[0]
    for a in arr[1:]:
        if a - m > ans: ans = a - m
        if a > ans: ans = a
        if m > a: m = a
            
    return ans

def main():
    _ = int(input())
    arr = list(map(int, input().split(" ")))
    DP(arr)
    ans = calculate(arr)
    print(ans)
    
main()