import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split(" "))
A = sorted(list(map(int, input().strip().split(" "))))
B = sorted(list(map(int, input().strip().split(" "))))

def find(target):
    global B
    s, e = 0, len(B)-1
    mid = (s+e)//2
    while(s <= e):
        mid = (s+e)//2
        if(target == B[mid]):
            return mid
        elif(target < B[mid]):
            e = mid-1
        else:
            s = mid+1
    return -1

ans = []
for a in A:
    if find(a) == -1:
        ans.append(a)
print(len(ans))
print(" ".join(list(map(str, ans))))