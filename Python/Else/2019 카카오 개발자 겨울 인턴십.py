# n = 500
def solution(s):
    answer = []
    arr = []
    stack = []
    flag = False
    tmp = ""
    for c in s[1:len(s)-1]:
        if c == "{":
            flag = True
        elif c == "," and flag:
            stack.append(int(tmp))
            tmp = ""
        elif c == "}":
            stack.append(int(tmp))
            tmp = ""
            arr.append(stack)
            stack = []
            flag = False
        elif c == ",": continue
        else:
            tmp += c
    arr.sort(key=lambda x: len(x))
    tmp = set([])
    for a in arr:
        for b in a:
            if b not in tmp:
                tmp.add(b)
                answer.append(b)
                break
                
    return answer
