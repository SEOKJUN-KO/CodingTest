https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3#

def solution(name):
    answer = float('inf')
    ans = 0
    for n in name:
        if(ord(n) <= ord('N')):
            ans += ord(n)-ord('A')
        else:
            ans += ord('Z')-ord(n)+1
    if(ans == 0): return 0
    answer = min(ans+len(name)-1, answer)
    idx = -1
    for i in range(len(name)):
        tmp = ans
        if(name[i+1:] == 'A'*len(name[i+1:])):
            tmp += i
            if(answer > tmp):
                answer = tmp
            continue
        tmpIdx = 0
        if( i + 1 < len(name) and name[i+1] == 'A'):
            tmpIdx = i+1
            while(tmpIdx+1 < len(name) and name[tmpIdx+1] == 'A'):
                tmpIdx += 1
        tmp += 2*(i)+(len(name)-1)-tmpIdx
        if(answer > tmp):
            answer = tmp
    name = name[::-1]
    for i in range(len(name)):
        tmp = ans+1
        if(name[i+1:] == 'A'*len(name[i+1:])):
            tmp += i
            if(answer > tmp):
                answer = tmp
            continue
        tmpIdx = 0
        if( i + 1 < len(name) and name[i+1] == 'A'):
            tmpIdx = i+1
            while(tmpIdx+1 < len(name) and name[tmpIdx+1] == 'A'):
                tmpIdx += 1
        tmp += 2*(i)+(len(name)-1)-tmpIdx
        if(answer > tmp):
            answer = tmp
    return answer
