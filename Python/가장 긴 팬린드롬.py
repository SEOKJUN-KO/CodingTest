def solution(s):
    answer = 1
    left, right = 0, len(s)-1
    while( left <= right and 0 <= left < len(s) and 0 <= right < len(s) ):
        if right-left+1 <= answer:
            left += 1
            right = len(s)-1
            continue
        if s[left] == s[right]:
            tmpL, tmpR = left+1, right-1
            flag = False
            while(tmpL <= tmpR):
                if s[tmpL] != s[tmpR]:
                    flag = True
                    break
                tmpL += 1
                tmpR -= 1
            if flag:
                right -= 1
                if left == right:
                    left += 1
                    right = len(s)-1
            else:
                if answer < right-left+1: answer = right-left+1
                left += 1
                right = len(s)-1
        else:
            right -= 1
            if left == right:
                left += 1
                right = len(s)-1
                    
    return answer
