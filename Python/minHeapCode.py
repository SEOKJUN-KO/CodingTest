import sys

N = int(sys.stdin.readline())
mHeap = [0]

def hAdd(inp):
    mHeap.append(inp)
    idx = len(mHeap)-1
    while(idx//2 >= 1):
        if(mHeap[idx] < mHeap[idx//2]):
            mHeap[idx], mHeap[idx//2] = mHeap[idx//2], mHeap[idx]
            idx = idx//2
        else:
            break

def hErase():
    if(len(mHeap) == 1):
        return 0
    mHeap[1], mHeap[-1] = mHeap[-1], mHeap[1]
    out = mHeap[-1]
    mHeap.pop()
    idx = 1
    while(2*idx < len(mHeap)):
        left, right = 2*idx, 2*idx+1
        if(right < len(mHeap)):
            if(mHeap[idx] > mHeap[left] and mHeap[left] <= mHeap[right]):
                mHeap[idx], mHeap[left] = mHeap[left], mHeap[idx]
                idx = left
            elif(mHeap[idx] > mHeap[right] and mHeap[right] < mHeap[left]):
                mHeap[idx], mHeap[right] = mHeap[right], mHeap[idx]
                idx = right
            else:
                break
        else:
            if(mHeap[idx] > mHeap[left]):
                mHeap[idx], mHeap[left] = mHeap[left], mHeap[idx]
                idx = left
            else:
                break
    return out
for _ in range(N):
    i = int(sys.stdin.readline())
    if(i != 0):
        hAdd(i)
    else:
        print(hErase())
