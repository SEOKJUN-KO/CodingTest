import math
dic = {}

def hourToMin(time):
    h, m = time.split(":")
    return int(h)*60+int(m)

def getADD(flowTime, under, term, addCost):
    return math.ceil( (flowTime-under)/term ) * addCost

def calculate(fees, records):
    global dic, totalD
    under, basic, term, addCost = fees
    
    arr = []
    for record in records:
        time, car, typ = record.split(" ")
        total = hourToMin(time)
        if typ == 'IN':
            if car not in dic.keys(): dic[car] = [0, -1]
            dic[car][1] = total
        elif typ == 'OUT':
            dic[car][0] += total - dic[car][1]
            dic[car][1] = -1
    keyList = list(dic.keys())
    keyList = sorted(keyList, key=lambda x: x)
    answer = []
    
    for key in keyList:
        tmp = basic
        if dic[key][1] != -1:
            dic[key][0] += hourToMin('23:59') - dic[key][1]
            dic[key][1] = -1

        if dic[key][0] > under:
            tmp += getADD(dic[key][0], under, term, addCost)
        answer.append(tmp)
    return answer
    
def solution(fees, records):
    return calculate(fees, records)