from collections import deque

N, K = map(int, input().split() )
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
        if( 0 <= 2*x < 200000 ):
            if( arr[2*x] == -1 ):
                arr[2*x] = w
                que.append([2*x, w])
        for X in (x-1, x+1):
            if( 0 <= X < 100001 ):
                if( arr[X] == -1 ):
                    arr[X] = w+1
                    que.append([X, w+1])
    
print(BFS())
