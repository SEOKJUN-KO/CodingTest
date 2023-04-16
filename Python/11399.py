N = int(input())

arr = list(map(int, input().split()))
arr = sorted(arr)
s, ans = 0, []
for a in arr:
    s += a
    ans.append(s)
print(sum(ans))
