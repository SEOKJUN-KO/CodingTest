// https://school.programmers.co.kr/learn/courses/30/lessons/148653?language=python3#
def solution(storey):
    ans = 0
    while(storey > 0):
        n = storey%10
        storey = storey//10
        st = str(storey)
        if(n>5):
            ans += 10-n
            storey += 1
        elif(n<5):
            ans += n
        else:
            ans += 5
            flag = 0
            for c in st[::-1]:
                if(int(c) == 5):
                    flag = 0
                    continue
                elif(int(c) > 5):
                    flag = 1
                    storey += 1
                    break
                else:
                    flag = 2
                    break
            if(flag == 0): storey += 1
    return ans
