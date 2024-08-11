import sys

rootDic = {}
nodeDic = {}

class Node:
    def __init__(self, mid, color, maxDepth):
        self.mid = mid
        self.color = color
        self.maxDepth = maxDepth
        self.child = []

def addNode(mid, pid, color, maxDepth):
    node = Node(mid, color, maxDepth)
    if pid == -1:
        rootDic[mid] = node
        return
    flag = False
    depth = maxDepth
    if pid in rootDic.keys():
        pNode = rootDic[pid]
        depth = min(depth, pNode.maxDepth-1)
        node.maxDepth = depth
        if depth >= 1:
            pNode.child.append(mid)
            flag = True
    else:
        depth = min(depth, nodeDic[pid].maxDepth-1)
        node.maxDepth = depth
        if depth >= 1:
            nodeDic[pid].child.append(mid)
            flag = True
    if flag:
        nodeDic[mid] = node

def changeColor(mid, color):
    if mid in rootDic.keys():
        rootDic[mid].color = color
        for child in rootDic[mid].child:
            changeColor(child, color)
        return
    nodeDic[mid].color = color
    for child in nodeDic[mid].child:
        changeColor(child, color)
    return

def viewColor(mid):
    if mid in rootDic.keys():
        print(rootDic[mid].color)
        return
    print(nodeDic[mid].color)

cnt = 0
def calculate(mid):
    global cnt
    s = set()
    if mid == -1:
        for rid in rootDic.keys():
            for child in rootDic[rid].child:
                s |= calculate(child)
            s.add(rootDic[rid].color)
            cnt += len(s)*len(s)
            s = set()
        return
    for child in nodeDic[mid].child:
        s |= calculate(child)
    s.add(nodeDic[mid].color)
    cnt += len(s)*len(s)
    return s
    

input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    order = list(map(int, input().split(" ")))
    if order[0] == 100:
        (mid, pid, color, maxDepth) = (order[1], order[2], order[3], order[4])
        addNode(mid, pid, color, maxDepth)
    elif order[0] == 200:
        (mid, color) = (order[1], order[2])
        changeColor(mid, color)
    elif order[0] == 300:
        viewColor(order[1])
    else:
        cnt = 0
        calculate(-1)
        print(cnt)
