def solution(s):
    ans = ""
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    tmp = ""
    for c in s:
        if c.isdigit():
            ans += c
            continue
        tmp += c
        if tmp in dic.keys():
            ans += dic[tmp]
            tmp = ""
    if tmp in dic.keys():
        ans += dic[tmp]
        tmp = ""
    return int(ans)
