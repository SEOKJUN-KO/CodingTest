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
    i, j = 0, 0
    merged = []
    N, M = len(left), len(right)
    while(N + M != len(merged)):
            if(i == N):
                merged.append(right[j])
                j += 1
            elif(j == M):
                merged.append(left[i])
                i += 1
            else:
                if(left[i] <= right[j]):
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
    return merged
    
ans = mergeSort(arr)
for a in ans:
    print(a)
