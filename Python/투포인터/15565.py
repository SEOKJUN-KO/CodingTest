def twoPointer(arr: list, K):
    ans = float('inf')
    l, r = 0, 0
    c = 0
    while(True):
        if arr[r] == 1:
            c += 1
            if c == K:
                if ans > (r-l+1):
                    ans = r-l+1
                while(True):
                    if arr[l] == 1:
                        c -= 1
                    l += 1
                    if (l == len(arr)):
                        break
                    if c == K-2:
                        l -= 1
                        c += 1
                        break
        r += 1
        if r == len(arr): break
    return ans

def main():
    _, K = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    ret = twoPointer(arr, K)
    if (ret == float('inf')): print(-1)
    else: print(ret)
main()