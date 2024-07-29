import sys
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A = sorted(A)
added = []
for a in range(len(A)-1):
    for b in range(a, len(A)-1):
        added.append(A[a]+A[b])
added = sorted(list(set(added)))

def search(start, end, n):
    while(start<=end):
        mid = (start+end)//2
        if(added[mid] == n):
            return 1
        elif(added[mid]>n):
            start, end = start, mid-1
        else:
            start, end = mid+1, end
    return 0

for a in range(len(A)-1, 0, -1):
    for b in range(a, 0, -1):
        q = search(0, len(added), A[a] - A[b])
        if(q == 1):
            print(A[a])
            exit()
