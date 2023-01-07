from collections import deque

N, K = map(int, input().split() )
arr = [-1]*(200001)

def BFS():
    global N, K
    que = deque()
    que.append([N, 0])
    arr[N] = 0
    ans = []
    while(que):
        x, w = que.popleft()
        if(x == K):
            while(x != N):
                ans.append(x)
                x = arr[x]
            return ans
        for X in (x-1, x+1, 2*x):
            if( 0 <= X < 200001 ):
                if( arr[X] == -1 ):
                    arr[X] = x
                    que.append([X, w+1])
    
ans = BFS()
ans.append(N)
ans.reverse()
print(len(ans)-1)
print(" ".join(str(n) for n in ans ))
