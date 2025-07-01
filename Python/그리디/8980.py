import sys

input = sys.stdin.readline
N, C = map(int, input().strip().split(" "))
M = int(input())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().strip().split(" "))))

village = [ {} for _ in range(N+1) ] # 2*10^3
for start, end, total in arr: # 10^4
    if end not in village[start].keys(): village[start][end] = 0
    village[start][end] += total

ans = 0
canLift = C
truck = {}
for now in range(1, N+1):
    if now in truck.keys():
        downBox = truck[now]
        del(truck[now])
        canLift += downBox
        ans += downBox
    keyList = sorted(list(set(list(truck.keys())+list(village[now].keys()))))
    
    newTruck = {}
    canLift = C
    for key in keyList:
        newTruck[key] = 0
        if key in truck.keys():
            upBox = min(truck[key], canLift)
            canLift -= upBox
            newTruck[key] += upBox
        if key in village[now]:
            upBox = min(village[now][key], canLift)
            canLift -= upBox
            newTruck[key] += upBox
        if canLift == 0: break
    truck = newTruck
print(ans)
    
    