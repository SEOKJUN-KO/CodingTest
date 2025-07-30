import sys

input = sys.stdin.readline
ans = 0
def collectJadu(T):
    arr = []
    now = 0
    cnt = 0
    for i in range(T):
        n = int(input())
        if n == now+1: 
            cnt += 1
            if i == T-1:
                tmp = [0, 0]
                tmp[now] = cnt
                arr.append(tmp)
        else:
            tmp = [0, 0]
            tmp[now] = cnt
            arr.append(tmp)
            now = (now+1)%2
            cnt = 1
    return arr


def cleanUp(ex, idx):
    keyArr = sorted(list(ex[idx].keys()))
    bigArr = keyArr[::-1]
    for a in keyArr:
        for b in bigArr:
            if a == b: break
            if a < b and ex[idx][a] <= ex[idx][b]:
                del(ex[idx][a])
                break

def caculate(ex, idx, next, N):
    global ans
    for key in ex[idx].keys():
        ex[idx][key] += N
        if ans < ex[idx][key]: ans = ex[idx][key]
    for key in ex[next].keys():
        if key - 1 >= 0:
            C = ex[next][key] + N
            if key-1 not in ex[idx].keys(): 
                ex[idx][key-1] = C
            else:
                ex[idx][key-1] = max(ex[idx][key-1], C)
            if ans < ex[idx][key-1]: ans = ex[idx][key-1]
    cleanUp(ex, idx)
    return


def dp(arr, W):
    ex = [{W: 0}, {W-1: 0}]
    for a in arr:
        one, two = a
        caculate(ex, 0, 1, one)
        caculate(ex, 1, 0, two)
    return

def main():
    global ans
    T, W = map(int, input().split(" "))
    arr = collectJadu(T)
    dp(arr, W)
    print(ans)
    return

main()