import sys
input = sys.stdin.readline

score = 0
class Node:
    def __init__(self, mid, pid, color, maxDepth):
        self.mid = mid
        self.pid = pid
        self.color = color
        self.maxDepth = maxDepth
        self.childList = []
        
    def addChild(self, node):
        if self.maxDepth == 1: return False
        depth = min(self.maxDepth-1, node.maxDepth)
        node.changeDepth(depth)
        self.childList.append(node)
        return True

    def changeDepth(self, depth):
        self.maxDepth = depth

    def changeColor(self, color):
        self.color = color
        for child in self.childList:
            child.changeColor(color)
    
    def showColor(self):
        print(self.color)

    def calculateScore(self):
        global score
        s = set([])
        s.add(self.color)
        for child in self.childList: s |= child.calculateScore()
        score += len(s)*len(s)
        return s

nodeD = {}
rootD = {}
def makeNode(mid, pid, color, maxDepth):
    node = Node(mid, pid, color, maxDepth)
    if pid == -1:
        rootD[mid] = node
        nodeD[mid] = node
        return
    parent = nodeD[pid]
    if parent.addChild(node):
        nodeD[mid] = node

Q = int(input())
for _ in range(Q):
    inp = list(map(int, input().split(" ")))
    if inp[0] == 100:
        mid, pid, color, maxDepth = inp[1], inp[2], inp[3], inp[4]
        makeNode(mid, pid, color, maxDepth)
    elif inp[0] == 200:
        mid, color = inp[1], inp[2]
        node = nodeD[mid]
        node.changeColor(color)
    elif inp[0] == 300:
        mid = inp[1]
        node = nodeD[mid]
        node.showColor()
    elif inp[0] == 400:
        score = 0
        for root in rootD.keys():
            node = nodeD[root]
            node.calculateScore()
        print(score)
