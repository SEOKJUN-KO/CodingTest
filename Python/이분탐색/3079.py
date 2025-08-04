import sys
input = sys.stdin.readline
# M명 = 10^9 -> 이분탐색
# N 입국 심사대 = 10^5

def makeArr(N):
    arr = []
    for _ in range(N): 
        arr.append(int(input()))
    arr = sorted(arr, key=lambda x: x)
    return arr

def bisectTime(arr, M):
    s, e = 0, 10**18
    ans = float('inf')
    while(s <= e):
        mid = (s+e)//2
        cnt = 0
        for a in arr:
            cnt += mid//a
            if cnt >= M:
                if ans > mid: ans = mid
                e = mid-1
                break
        if e != mid-1: s = mid+1
    return ans



def main():
    N, M = map(int, input().split(" "))
    arr = makeArr(N)
    print(bisectTime(arr, M))
    
main()