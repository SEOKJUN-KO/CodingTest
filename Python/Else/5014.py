from collections import deque
F, S, G, U, D = map(int, input().split())

arr = [0]*(F+1)
que = deque()
que.append([S, 0])
arr[S] = -1
while(que):
    c, w = que.popleft()
    if(c == G):
        print(w)
        exit()
    u = c + U
    d = c - D
    if( 1 <= u <= F and arr[u] == 0 ):
        arr[u] = -1
        que.append([u, w+1])
    if( 1 <= d <= F and arr[d] == 0 ):
        arr[d] = -1
        que.append([d, w+1])
print("use the stairs")
