import sys
from collections import deque
sys.setrecursionlimit(10**6)

dic = {}
keys = {}
level = 0
answer = [[]]
class Node:
    def __init__(self, v, y, x):
        self.left = None
        self.right = None
        self.parent = None
        self.value = v
        self.y = y
        self.x = x
        
def leftChild(node, leftArr, rightArr):
    global dic, keys, level
    # print("left", node.value, leftArr, rightArr)
    
    if level >= len(dic.keys()): return
    
    if len(dic[keys[level]]) == 0: return

    for left in leftArr:
        if dic[keys[level]][0].x > left: return
    
    for right in rightArr:
        if dic[keys[level]][0].x < right: return
    
    leftN = dic[keys[level]].popleft()
    node.left = leftN
    leftN.parent = node
    # print(leftN.value)
    level += 1
    leftChild(leftN, leftArr+[leftN.x], rightArr)
    rightChild(leftN, leftArr, rightArr+[leftN.x])
    level -= 1
    
def rightChild(node, leftArr, rightArr):
    global dic, keys, level
    # print("right", node.value, leftArr, rightArr)
    
    if level >= len(dic.keys()): return
    
    if len(dic[keys[level]]) == 0: return

    for left in leftArr:
        if dic[keys[level]][0].x > left: return
    
    for right in rightArr:
        if dic[keys[level]][0].x < right: return
    
    rightN = dic[keys[level]].popleft()
    node.right = rightN
    rightN.parent = node
    # print(rightN.value)
    
    level += 1
    leftChild(rightN, leftArr+[rightN.x], rightArr)
    rightChild(rightN, leftArr, rightArr+[rightN.x])
    level -= 1

def make1(node):
    global answer
    answer[0].append(node.value)
    if node.left != None: make1(node.left)
    if node.right != None: make1(node.right)

def make2(node):
    global answer
    if node.left != None: make2(node.left)
    if node.right != None: make2(node.right)
    answer[1].append(node.value)
    
def solution(nodeinfo):
    global dic, keys, level, answer
    
    nodeList = []
    for i in range(len(nodeinfo)):
        x = nodeinfo[i][0]; y = nodeinfo[i][1]
        nodeList.append([y, x, i+1])
    nodeList = sorted(nodeList, key=lambda x: (-x[0], x[1]))
    for y, x, v in nodeList:
        if y not in dic.keys(): dic[y] = deque()
        node = Node(v, y, x)
        dic[y].append(node)
    keys = sorted(dic.keys(), key = lambda x: -x)
    node = dic[keys[level]][0]; leftArr = [node.x]; rightArr = [node.x]
    level += 1
    leftChild(node, leftArr, [])
    rightChild(node, [], rightArr)
    level -= 1
    make1(node)
    answer.append([])
    make2(node)
    
    return answer
