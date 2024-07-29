N, C = map(int, input().split())
dic = {}
arr = list(map(int, input().split()))

for a in arr:
    dic[a] = dic.get(a, 0) + 1
key = dic.keys()
ans = sorted(key, key = lambda x : -dic[x])
for k in ans:
    for _ in range(dic[k]):
        print(k, end=" ")
