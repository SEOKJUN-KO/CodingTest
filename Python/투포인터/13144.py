import sys; input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))
s = set([])
left, right = 0, 1
s.add(arr[0])
ans = 0
while(left<=right and right < N):
    if arr[right] not in s:
        s.add(arr[right]); right += 1
    else:
        ans += len(s)
        s.remove(arr[left]); left += 1
ans += (len(s)*(len(s)+1))//2
print(ans)
