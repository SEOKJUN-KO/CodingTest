N = int(input())

arr = []
def hanoi(s, m, e, n):
    if(n == 0):
        return
    hanoi(s, e, m, n-1)
    arr.append([s, e])
    hanoi(m, s, e, n-1)
hanoi(1, 2, 3, N)
print(len(arr))
for a in arr:
    print(" ".join(map(str, a)))
