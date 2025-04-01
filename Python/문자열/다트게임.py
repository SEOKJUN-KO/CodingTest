def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def solution(dartResult):
    scores = []
    tmp = ""
    flag = False
    for d in dartResult:
        if is_number(d) and flag:
            tmp = d
            flag = False
        elif is_number(d) and not flag:
            tmp += d
        else:
            if is_number(tmp):
                bonus = 0
                if d == "S": bonus = 1
                elif d == "D": bonus = 2
                else: bonus = 3
                scores.append(int(tmp)**(bonus))
                tmp = ""
                flag = False
            else:
                if d == "#":
                    scores[-1] *= -1
                else:
                    scores[-1] *= 2
                    if len(scores) >= 2:
                        scores[-2] *= 2
    return sum(scores)