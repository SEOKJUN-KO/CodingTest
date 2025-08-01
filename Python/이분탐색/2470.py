from bisect import bisect_left

def find(a, arr):
    ret = [float('inf'), -1]
    idx = bisect_left(arr, -1*a)
    for i in [idx-1, idx, idx+1]:
        if 0 <= i < len(arr) and a!= arr[i] and (abs(arr[i]+a) < abs(ret[0])):
            ret = [arr[i]+a, arr[i]]
    return ret

def main():
    _ = int(input())
    ans = [float('inf'), []]
    arr = list(map(int, input().split(" ")))
    arr = sorted(arr)
    for a in arr:
        ret = find(a, arr)
        # print(a, ret[1], ret[0])
        if ans[0] > abs(ret[0]):
            ans = [abs(ret[0]), [a, ret[1]]]
    ans[1] = sorted(ans[1])
    print(ans[1][0], ans[1][1])
main()