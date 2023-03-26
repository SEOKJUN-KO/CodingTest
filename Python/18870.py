n = input()
B = list(map(int, input().split()))
A = set(B)
A = sorted(list(A))
def lowerSearch(target):
    start, end = 0, len(A)
    while(start<end):
        mid = (start+end)//2
        if(A[mid] < target):
            start = mid+1
        else:
            end = mid
    return start
ans = []
for b in B:
    ans.append(lowerSearch(b))
print(" ".join(map(str,ans)))
