N, K = map(int, input().split(" "))
S = list(map(int, input().split(" ")))

left, right = 0, 0
cntO, cntE = 0, 0
ans = 0
if S[0]%2 == 1:
    cntO = 1
else:
    cntE = 1
    ans = 1
while( left <= right and right < len(S) ):
    if left == right or cntO <= K:
        right += 1
        if right == len(S): break
        if S[right]%2 == 1:
            cntO += 1
        else:
            cntE += 1
            ans = max(cntE, ans)
    else:
        if S[left]%2 == 1:
            cntO -= 1
        else:
            cntE -= 1
        left += 1
print(ans)
