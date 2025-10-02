def solution(survey, choices):
    answer = ''
    dic = {}
    for c in "RTCFJMAN":
        dic[c] = 0
    for i in range(len(survey)):
        sur = survey[i]
        score = choices[i]
        add = ""
        if (score <= 3):
            add = sur[0]
            score = abs(score-4)
        elif(score == 4):
            continue
        else:
            add = sur[1]
            score -= 4
        dic[add] += score

    for A, B in [ ['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]:
        if dic[A] >= dic[B]: answer += A
        else: answer += B
    
    return answer