N, M = map(int, input().split())
Arr = list(map(int, input().split()))
Brr = list(map(int, input().split()))
ans = []
i, j = 0, 0
while(len(ans) != N+M):
    if(i == N):
        ans.append(Brr[j])
        j += 1
    elif(j == M):
        ans.append(Arr[i])
        i += 1
    else:
        if(Arr[i] < Brr[j]):
            ans.append(Arr[i])
            i += 1
        else:
            ans.append(Brr[j])
            j += 1
print(" ".join(map(str, ans)))
