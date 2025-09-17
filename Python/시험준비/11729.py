cnt = 0
ans = []

def goTo(now, target, plate):
    global cnt 
    cnt += 1
    if plate == 1:
        ans.append(str(now)+" "+str(target))
        return
        
    goTo(now, 6 - now - target, plate-1)
    ans.append(str(now)+" "+str(target))
    goTo(6- now - target, target, plate-1)

def solution():
    global cnt, ans
    n = int(input())
    goTo(1, 3, n)
    print(cnt)
    for a in ans:
        print(a)
solution()