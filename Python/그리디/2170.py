import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N): arr.append(list(map(int, input().split(" "))))
arr.sort()

line = []; tmp = arr[0]
for a in arr[1:]:
    if (a[0] <= tmp[1]) and (tmp[1] <= a[1]):
        tmp = [tmp[0], a[1]]
    elif (tmp[0] <= a[0]) and (a[1] <= tmp[1]):
        tmp = [tmp[0], tmp[1]]
    else:
        line.append(tmp)
        tmp = a
        
ans = 0
for l in line:
    ans += l[1]-l[0]
if line == [] or (line != [] and line[-1] != tmp):
    ans += tmp[1]-tmp[0]
    
print(ans)
