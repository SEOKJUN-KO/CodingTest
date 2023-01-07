from collections import deque

N, K = map(int, input().split() )
if(N == K):
    print(0)
    exit()

arr = [-1]*(200001)

def BFS():
    global N, K
    que = deque()
    que.append([N, 0])
    arr[N] = 0
    while(que):
        x, w = que.popleft()
        if(x == K):
            return w
        ox = x-1
        tx = x+1
        thx = 2*x
        if( 0 <= thx < 200000 ):
            if( arr[thx] == -1 ):
                arr[thx] = w
                que.append([thx, w])
        if( 0 <= ox < 100001 ):
            if( arr[ox] == -1 ):
                arr[ox] = w+1
                que.append([ox, w+1])
        if( 0 <= tx < 100001 ):
            if( arr[tx] == -1 ):
                arr[tx] = w+1
                que.append([tx, w+1])
    
print(BFS())
