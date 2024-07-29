word = input().strip()
arr = []

for i in range(len(word)):
    arr.append(word[i:])
ans = sorted(arr)
for a in ans:
    print(a)
