# 자식노드가 1인데, 부모노드 부분에서 0이면 실패
# 문자열 부족하다면 앞에 0 추가
def divide(st):
    l = len(st)
    if l == 1:
        return [st, True]
    left = divide(st[:l//2])
    right = divide(st[l//2+1:])
    if not (left[1] and right[1]):
        return ["", False]
    if st[l//2] == "0" and left[0] == "0" and right[0] == "0":
        return ["0", True]
    if st[l//2] == "0" and (left[0] == "1" or right[0] == "1"):
        return ["", False]
    return ["1", True]
    
def solution(numbers):
    ans = []
    for number in numbers:
        number = bin(number).split("b")[1]
        if number == "0":
            ans.append(0)
            continue
        cnt, i = 1, 1
        while(cnt < len(number)):
            cnt += 2**i
            i += 1
        number = "0"*(cnt-len(number)) + number
        out = divide(number)
        if out[1]: ans.append(1)
        else: ans.append(0)
    return ans
