from collections import deque

n = int(input())
arr = list(map(int, input().split()))
visited = [False]*(n)
s = int(input())
s -= 1

que = deque([])
que.append(s)
visited[s] = True
ans = 1
while(que):
    now = que.popleft()
    if( now - arr[now] >= 0 and visited[now - arr[now]] == False ):
        ans += 1
        visited[now - arr[now]] = True
        que.append(now - arr[now])
    if( now + arr[now] < n and visited[now + arr[now]] == False ):
        ans += 1
        visited[now + arr[now]] = True
        que.append(now + arr[now])
print(ans)
