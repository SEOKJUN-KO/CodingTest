import sys
input = sys.stdin.readline

def bisectSize(arr, N, M):
    s, e = max(arr), 9999999999999999
    ans = float('inf')
    while(s <= e):
        mid = (s+e)//2
        block = 0
        cnt = 0
        for i in range(N):
            a = arr[i]
            cnt += a
            if cnt == mid:
                block += 1
                cnt = 0
            elif cnt > mid:
                block += 1
                cnt = a
            if block > M:
                break
        if cnt > 0: block += 1
        if block > M:
            s = mid + 1
        elif block < M:
            if ans > mid: ans = mid
            e = mid - 1
        else:
            if ans > mid: ans = mid
            e = mid - 1
    return ans

def main():
    N, M = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    ans = bisectSize(arr, N, M)
    print(ans)
main()