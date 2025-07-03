while(True):
    while(True):
        now, n = arr[rightP]
        if save[now] == 0:
            cnt += 1
        save[now] += 1
        rightP += 1
        if cnt == N: break
        if rightP == N*M: break

    while(True):
        now, n = arr[leftP]
        save[now] -= 1
        cnt -= 1
        leftP += 1
        if cnt+1 == N: break
        if leftP == N*M: break
    
    if (rightP < leftP or rightP == N*M): break
    print(arr[leftP], arr[rightP])