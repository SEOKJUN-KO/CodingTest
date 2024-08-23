import sys
input = sys.stdin.readline

class Knight:
    def __init__(self, r, c, h, w, k):
        self.y = r
        self.x = c
        self.height = h
        self.width = w
        self.health = k
        self.damage = 0

L = 0; board = []; knightB = []; dic = {}
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0] # 상, 우, 하, 좌
pushOk = True; store = []
def push(idx, direct):
    global dic, L, pushOk, board, knightB, store
    knight = dic[idx]
    if knight.health <= knight.damage: return
    ny, nx, width, height = knight.y, knight.x, knight.width, knight.height
    tmp = []
    if direct == 0: #상
        for x in range(nx, nx+width): tmp.append([x, ny])
    elif direct == 1: #우
        for y in range(ny, ny+height): tmp.append([nx+width-1, y])
    elif direct == 2: #하
        for x in range(nx, nx+width): tmp.append([x, ny+height-1])
    else: #좌
        for y in range(ny, ny+height): tmp.append([nx, y])
    for x, y in tmp:
        X, Y = x+dx[direct], y+dy[direct]
        if 0 <= X < L and 0 <= Y < L and knightB[Y][X] != 0:
            if knightB[Y][X] not in store: push(knightB[Y][X], direct)
            if not pushOk: return
        elif (0 <= X < L and 0 <= Y < L and board[Y][X] == 2) or not( 0 <= X < L and 0 <= Y < L ):
            pushOk = False; return
    store.append(idx)
    return

L, N, Q = map(int, input().split(" "))
knightB = [ [0]*L for _ in range(L) ]
for _ in range(L): board.append(list(map(int, input().split(" "))))

for i in range(1, N+1):
    r, c, h, w, k = map(int, input().split(" "))
    for y in range(h):
        for x in range(w):
            knightB[r-1+y][c-1+x] = i
    dic[i] = Knight(r-1, c-1, h, w, k)

for _ in range(Q):
    i, d = map(int, input().split(" "))
    pushOk = True; store = []
    push(i, d)
    if pushOk:
        for idx in store:
            knight = dic[idx]
            ny, nx, width, height = knight.y, knight.x, knight.width, knight.height
            delete = False
            for y in range(ny, ny+height):
                for x in range(nx, nx+width):
                    X, Y = x+dx[d], y+dy[d]
                    if board[Y][X] == 1 and idx != i:
                        knight.damage += 1
                        if knight.health <= knight.damage: delete = True; break
                if delete: break
            if delete:
                for y in range(ny, ny+height):
                    for x in range(nx, nx+width):
                        knightB[y][x] = 0
            else:
                for y in range(ny, ny+height):
                    for x in range(nx, nx+width):
                        knightB[y][x] = 0
                knight.y, knight.x = ny+dy[d], nx+dx[d]
                for y in range(ny, ny+height):
                    for x in range(nx, nx+width):
                        X, Y = x+dx[d], y+dy[d]
                        knightB[Y][X] = idx
ans = 0
for key in dic.keys():
    if dic[key].health > dic[key].damage: ans += dic[key].damage
print(ans)
