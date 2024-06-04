import sys
input = sys.stdin.readline

dic = {}
N = int(input())
Arr = list(map(int, input().split(" ")))
for a in Arr:
    if a not in dic.keys():
        dic[a] = 0
    dic[a] += 1
M = int(input())
Arr = list(map(int, input().split(" ")))
for a in Arr:
    if a not in dic.keys():
        print(0, end=" ")
    else:
        print(dic[a], end= " ")
