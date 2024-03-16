from collections import deque
def solution(maps):
    answer = 0
    maps = maps
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == 1: maps[y][x] = 300
            elif maps[y][x] == 0: maps[y][x] = -1
    dx, dy = [+1, +0, +0, -1], [+0, +1, -1, +0]
    que = deque()
    if maps[0][0] == 300: que.append([1, 0, 0])
    while(que):
        t, x, y = que.popleft()
        for i in range(4):
            X, Y = x+dx[i], y+dy[i]
            if 0 <= Y < len(maps) and 0 <= X < len(maps[Y]) and maps[Y][X] != -1:
                if maps[Y][X] > t+1:
                    maps[Y][X] = t+1
                    que.append([t+1, X, Y])
    if maps[-1][-1] == 300:
        return -1
    return maps[-1][-1]
