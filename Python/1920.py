N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A = sorted(A)

def search(start, end, n):
    while(start<=end):
        mid = (start+end)//2
        if(A[mid] == n):
            return 1
        elif(A[mid]>n):
            start, end = start, mid-1
        else:
            start, end = mid+1, end
    return 0
for b in B:
    print(search(0, len(A)-1, b))
