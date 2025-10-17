def solution(n, w, num):
    answer = 0
    L = n//w # 꽉 채워진 박스까지만 보겠다.
    level = -1 
    idx = -1
    for i in range(1, L+1):
        s = w*i-w+1
        e = w*i
        if s <= num <= e:
            level = i
            if i%2 == 1: idx = num-s
            else: idx = abs(num-e)
            break
    if level == -1: return 1 # 꽉 안 채워진 상자에 위치한 경우
    
    answer = (L)-level+1
    
    flag = ""
    if (L + 1)%2 == 1: flag="leftStart"
    else: flag ="rightStart"
    
    if n%w > 0:
        s = w*(L+1)-w+1
        e = min(w*(L+1), n)
        leftIdx = -1
        rightIdx = -1
        if flag == "leftStart":
            leftIdx = 0
            rightIdx = e-s
        else:
            rightIdx = w-1
            leftIdx = (w-1)-(e-s)
        if leftIdx <= idx <= rightIdx: 
            answer += 1
    return answer