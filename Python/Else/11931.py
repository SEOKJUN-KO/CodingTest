import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
    
def mergeSort(arr):
    if(len(arr) == 1):
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
    
def merge(left, right):
    L, R = len(left), len(right)
    i, j = 0, 0
    merged = []
    while(i < L and j < R):
        if(left[i] <= right[j]):
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
            
    while(i < L):
        merged.append(left[i])
        i += 1
    while(j < R):
        merged.append(right[j])
        j += 1
    return merged
ans = mergeSort(arr)
for a in ans:
    print(a)
