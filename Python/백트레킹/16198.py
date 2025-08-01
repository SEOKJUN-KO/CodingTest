ans = 0
def makeCase(arr, N, s):
    global ans
    if N == 2:
        if ans < s:
            ans = s
        return
    for i in range(1, N-1):
        store = arr[i]
        tmp = arr[i-1]*arr[i+1]
        s += tmp
        arr.pop(i)
        makeCase(arr, N-1, s)
        s -= tmp
        arr.insert(i, store)
        

def main():
    global ans
    N = int(input())
    arr = list(map(int, input().split(" ")))
    makeCase(arr, N, 0)
    print(ans)
main()