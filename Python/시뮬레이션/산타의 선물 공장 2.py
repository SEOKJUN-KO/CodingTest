import sys
input = sys.stdin.readline
from collections import deque
# m = 10^5


line = {}
box = {}
# 1. 공장 설립
# n 개의 벨트 / m 개의 물건
# 각 벨트에 오름차순으로 선물 쌓기
def appendRear(dst, boxN):
    global line, box
    if boxN not in box.keys():
        box[boxN] = [-1, -1]
    
    if len(line[dst]) == 0:
        line[dst].append(boxN)
        return
    
    last = line[dst].pop()
    line[dst].append(last)
    line[dst].append(boxN)
    box[last][1] = boxN
    box[boxN][0] = last
    


def makeFactory(arr):
    global line
    n, m = arr[1], arr[2]
    for i in range(1, n+1):
        line[i] = deque()
    
    idx = 1
    for i in arr[3:]:
        appendRear(i, idx)
        idx += 1
    
# 2. 물건 모두 옮기기
# m source -> m destination
# m dst = 앞 [ m src ] [ m dst ] 뒤
# 출력: m dst의 물건 수
def appendFront(dst, boxN):
    global line, box
    box[boxN] = [-1, -1]
    if len(line[dst]) == 0:
        line[dst].appendleft(boxN)
        return
    
    front = line[dst][0]
    line[dst].appendleft(boxN)
    box[front][0] = boxN
    box[boxN][1] = front

def popRear(dst):
    global line, box
    boxN = line[dst].pop()
    box[boxN] = [-1, -1]
    if len(line[dst]) > 0:
        last = line[dst].pop()
        box[last][1] = -1
        line[dst].append(last)
    return boxN
    
def moveAllStuff(arr):
    global line, box
    src, dst = arr[1], arr[2]
    while( line[src] ):
        appendFront(dst, popRear(src))
    print(len(line[dst]))

# 3. 앞 물건만 교체
# src 와 dst의 앞 물건만 교체
# 둘 중 하나 선물 아예 없다면 -> 해당 벨트로 선물 옮기기
# 출력: m dst의 물건 수
def popFront(dst):
    global line, box
    boxN = line[dst].popleft()
    box[boxN] = [-1, -1]
    if len(line[dst]) > 0:
        front = line[dst][0]
        box[front][0] = -1
    return boxN

def changeFirst(arr):
    global line, box
    src, dst = arr[1], arr[2]
    S = ''
    if len(line[src]) > 0: S = popFront(src)
    D = ''
    if len(line[dst]) > 0: D = popFront(dst)
    if S != '':  appendFront(dst, S)
    if D != '':  appendFront(src, D)
    print(len(line[dst]))

# 4. 물건 나누기
# src의 n//2 선물 앞에서 빼서, dst 앞에 두기
# 출력: m dst의 물건 수
# ?????? 옮기는 순서의 의문이 남음
def divideStuff(arr):
    global line, box
    src, dst = arr[1], arr[2]
    
    L = len(line[src])
    minus = len(line[src])//2 
    
    stack = [] # ??????
    while( len(line[src]) > L - minus ):
        stack.append( popFront(src) ) 
    while( len(stack) > 0 ):
        appendFront(dst, stack.pop())
    print(len(line[dst]))


# 5. 선물 정보 얻기
# 선물 번호
# 출력: 앞 뒤 선물 번호 계산 [ 앞 + 뒤*2 ] 출력 ( 없다면 각각 -1 )
def getStuffInfo(arr):
    global box
    p = arr[1]
    a, b = box[p]
    print( a + 2*b )

# 6. 벨트 정보 얻기
# 벨트 번호, 
# 출력: 맨앞 + 2*맨뒤 + 3* 갯수 ( 없다면 각각 -1 갯수는 0)
def getBeltInfo(arr):
    global line
    beltN = arr[1]
    c = len(line[beltN])
    a = -1
    if c > 0: a = line[beltN][0]
    b = -1
    if c > 0: 
        b = line[beltN].pop()
        line[beltN].append(b)

    print( a + 2*b + 3*c )

def main():
    q = int(input().strip())
    
    for _ in range(q):
        order = list(map(int, input().strip().split(" ")))
        if order[0] == 100:
            makeFactory(order)
        elif order[0] == 200:
            moveAllStuff(order)
        elif order[0] == 300:
            changeFirst(order)
        elif order[0] == 400:
            divideStuff(order)
        elif order[0] == 500:
            getStuffInfo(order)
        elif order[0] == 600:
            getBeltInfo(order)
main()