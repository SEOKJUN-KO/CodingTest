import sys
import heapq

input = sys.stdin.readline
dx, dy = [+1, -1, +0, +0], [+0, +0, +1, -1]
X, Y = map(int, input().split(" "))
visit = [[float('inf')]*X for _ in range(Y)]

board = []
for _ in range(Y):
    st = input().strip()
    tmp = []
    for c in st:
        tmp.append(int(c))
    board.append(tmp)
if Y+X <= 2: print(0)
else:
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visit[0][0] = 0
    
    while(heap):
        w, x, y = heapq.heappop(heap)
        if visit[y][x] < w: continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if ( 0 <= nx < X) and ( 0 <= ny < Y):
                if (visit[ny][nx] == float('inf')) or (visit[ny][nx] > board[ny][nx] + visit[y][x]):
                    visit[ny][nx] = board[ny][nx] + visit[y][x]
                    if ny == Y-1 and nx == X-1:
                        print(visit[ny][nx])
                        break
                    heapq.heappush(heap, [visit[ny][nx], nx, ny])
