import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.pre = None
        self.n = val
        self.next = None

class LL:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.pre = self.head

        self.size = 0
    
    def append(self, n: Node):
        n.pre = self.tail.pre
        n.next = self.tail

        self.tail.pre.next = n
        self.tail.pre = n

        self.size += 1
    
    def appendleft(self, n: Node):
        n.pre = self.head
        n.next = self.head.next

        self.head.next.pre = n
        self.head.next = n

        self.size += 1

    def getSize(self):
        return self.size
    
    def pop(self):
        n = self.tail.pre
        self.tail.pre = n.pre
        n.pre.next = self.tail

        n.pre = None
        n.next = None

        self.size -= 1
        return n

    def popleft(self):
        n = self.head.next
        self.head.next = n.next
        n.next.pre = self.head

        n.pre = None
        n.next = None

        self.size -= 1
        return n

    def getLast(self):
        return self.tail.pre
    
    def getFirst(self):
        return self.head.next
    
    def print(self):
        p = self.head.next
        while(p != self.tail):
            print(p.n, end="->")
            p = p.next
        print()
        
# m = 10^5


line = {}
box = {}
n = 0
m = 0

# 1. 공장 설립
# n 개의 벨트 / m 개의 물건
# 각 벨트에 오름차순으로 선물 쌓기
def appendRear(dst, boxN):
    global line, box
    node = Node(boxN)
    box[boxN] = node
    line[dst].append(node)
    
def checkState():
    global line, box, n, m
    for i in range(1, n+1):
        print(i, ":", end=" ")
        line[i].print()

    for i in range(1, m+1):
        print(i, ":", box[i].pre.n, box[i].next.n)

def makeFactory(arr):
    global line, box, n, m
    n, m = arr[1], arr[2]
    for i in range(1, n+1):
        line[i] = LL()
    
    idx = 1
    for i in arr[3:]:
        appendRear(i, idx)
        idx += 1
# 2. 물건 모두 옮기기
# m source -> m destination
# m dst = 앞 [ m src ] [ m dst ] 뒤
# 출력: m dst의 물건 수
def popRear(dst):
    global line
    return line[dst].pop()
    
def moveAllStuff(arr):
    global line, box
    src, dst = arr[1], arr[2]
    if line[src].getSize() > 0:
        # 기존 src에서 dst로 이어붙이기
        last = line[src].getLast()
        first = line[src].getFirst()
        
        # 뒷부분 연결
        line[dst].getFirst().pre = last
        last.next = line[dst].getFirst()
        
        # 앞 부분 연결
        line[dst].head.next = first
        first.pre = line[dst].head
        
        line[dst].size += line[src].size
        
        line[src].size = 0
        line[src].head.next = line[src].tail
        line[src].tail.pre = line[src].head        
    print(line[dst].getSize())

# 3. 앞 물건만 교체
# src 와 dst의 앞 물건만 교체
# 둘 중 하나 선물 아예 없다면 -> 해당 벨트로 선물 옮기기
# 출력: m dst의 물건 수
def popFront(dst):
    global line
    return line[dst].popleft()
    
def appendFront(dst, node):
    global line
    line[dst].appendleft(node)

def changeFirst(arr):
    global line, box
    src, dst = arr[1], arr[2]
    S = ''
    if line[src].getSize() > 0: S = popFront(src)
    D = ''
    if line[dst].getSize() > 0: D = popFront(dst)
    if S != '':  appendFront(dst, S)
    if D != '':  appendFront(src, D)
    
    print(line[dst].getSize())

# 4. 물건 나누기
# src의 n//2 선물 앞에서 빼서, dst 앞에 두기
# 출력: m dst의 물건 수
def divideStuff(arr):
    global line, box
    src, dst = arr[1], arr[2]
    
    L = line[src].getSize()
    minus = L//2 
    
    stack = []
    while( line[src].getSize() > L - minus ):
        stack.append( popFront(src) ) 
    while( len(stack) > 0 ):
        appendFront(dst, stack.pop())

    print(line[dst].getSize())


# 5. 선물 정보 얻기
# 선물 번호
# 출력: 앞 뒤 선물 번호 계산 [ 앞 + 뒤*2 ] 출력 ( 없다면 각각 -1 )
def getStuffInfo(arr):
    global box
    p = arr[1]
    a, b = box[p].pre.n, box[p].next.n
    print( a + 2*b )

# 6. 벨트 정보 얻기
# 벨트 번호, 
# 출력: 맨앞 + 2*맨뒤 + 3* 갯수 ( 없다면 각각 -1 갯수는 0)
def getBeltInfo(arr):
    global line
    beltN = arr[1]
    c = line[beltN].getSize()
    a = -1
    if c > 0: a = line[beltN].getFirst().n
    b = -1
    if c > 0: 
        b = line[beltN].getLast().n

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