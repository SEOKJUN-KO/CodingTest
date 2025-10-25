from api import startAPI, newRequestAPI, replyAPI, simulationAPI, scoreAPI
from heapq import heappush, heappop
from collections import deque

hotel = []
h = -1
w = -1
cancleN = 0
cancleM = 0
delay = 0
def makeHotel(mode):
    global hotel, h, w 
    if mode == 1:
        w = 20
        h = 3
    elif mode == 2:
        w = 200
        h = 10
    
    for y in range(h+1):
        tmp = []
        for _ in range(w+1):
            tmp.append(0)
        hotel.append(tmp)

waiting_heap = []
def addRequest(request_info, request_date):
    global waiting_heap
    for request in request_info:
        id, amount, check_in, check_out = request['id'], request['amount'], request['check_in_date'], request['check_out_date']
        heappush(waiting_heap, (-amount, check_in, request_date, check_out, id ) )

# 예약 관리 [ 알고리즘 ]
# 예약 요청 답변 기한 = min( 예약 요청 들어온 날짜 + 14, 체크인 날짜 - 1 ) 
    # 넘기면 예약 자동 거절
    # 같은 층에 연속된 객실을 제공할 수 있을 때, 승인

def denyRequest(today, c_in, req_date, id, amount):
    global cancleM, cancleN, delay
    if today - req_date >= 13:
        cancleM += amount
        cancleN += 1
        delay = today-req_date
        return {"id": id, "reply": "refused"}
    if c_in - today <= 1:
        cancleM += amount
        cancleN += 1
        delay = today-req_date
        return {"id": id, "reply": "refused"}
    return None

# 특정 기준보다 낮은 양의 예약이면, 날짜가 다가오는거가 아닌 이상 일단 넘긴다.
def shouldPass(today, amount, c_in, req_date, mode):
    global w 
    if mode == 1 and amount <= 3:
        if c_in - today <= 1:
            return False
        if today - req_date <= 12: # 8일까진 괜찮음 숫자 적으면, 예약 안 받아 줌
            return True
        return False
    if mode == 2 and amount <= 20:
        if c_in - today <= 1:
            return False
        if today - req_date <= 12: # 8일까진 괜찮음 숫자 적으면, 예약 안 받아 줌
            return True
        return False


accepted_heap = []
def checkReply(today, mode):
    global hotel, h, w, waiting_heap, accepted_heap, delay
    replies = []
    saved = []
    
    while(waiting_heap):
        m, c_in, req_date, c_out, id = heappop(waiting_heap)
        amount = -m
        # 초반에 작은 요청을 먼저 처리하면, 큰 친구들을 받아내지 못한다. -> 작은 요청이 급하지 않다면, 미뤄두기
        if shouldPass(today, amount, c_in, req_date, mode):
            saved.append((m, c_in, req_date, c_out, id))
            continue
        
        flag = True
        for y in range(1, h+1):
            for x in range(1, w+1):
                flag = True
                if x + amount -1 >= w+1:
                    # print(y, [c_in], "amount:", amount,"x:", x, "x+amount-1:", x+amount-1,"w:", w)
                    flag = False; break # 체크 완료
                for X in range(amount): # 체크아웃이 체크인보다 미래의 날짜면 안된다.
                    if hotel[y][x+X] > c_in:
                        flag = False; break
                if flag: # 체크아웃보다 체크인이 뒤 일때
                    replies.append({"id": id, "reply": "accepted"})
                    roomN = str(y)+str(x).zfill(3)
                    # print("accept", id, "today-req_date:", today-req_date, "c_in-today:", c_in-today, "amount:", amount)
                    delay += today - req_date
                    heappush(accepted_heap, ( c_in, id, roomN ))
                    for X in range(amount):
                        hotel[y][x+X] = c_out
                    break
            
            if y == h and flag == False: # 아무것도 하지 못했을 때
                ret = denyRequest(today, c_in, req_date, id, amount)
                if ret != None:replies.append(ret)
                else: saved.append((m, c_in, req_date, c_out, id))
            
            if flag: break
    
    while(saved):
        m, c_in, req_date, c_out, id = saved.pop()
        heappush(waiting_heap, (m, c_in, req_date, c_out, id))
                    
    return replies

def makeRoomAssign(today):
    global accepted_heap
    room_assign = []

    while(accepted_heap):
        if accepted_heap[0][0] > today: return room_assign # 오늘보다 예약 날짜가 미래인 것은 할당할 수 없다.
        c_in, id, roomN = heappop(accepted_heap) 
        room_assign.append({"id": id, "room_number": roomN})
        
    return room_assign

def isEnd(mode, today):
    global waiting_heap, accepted_heap
    if mode == 1:
        return (today <= 200 or waiting_heap or accepted_heap)
    elif mode == 2:
        return (today <= 1000 or waiting_heap or accepted_heap)

def solution(mode):
    global hotel, cancleN, cancleM, delay
    startAPI(mode)
    makeHotel(mode)
    present_day = 1

    while(isEnd(mode, present_day)):
        request_info = newRequestAPI() 
        addRequest(request_info, present_day) # 새로운 예약 정보를 담기
        replies = checkReply(present_day, mode) # 예약이 체크인 날짜에 가능할지 체크해서, 가능한 예약은 승낙, 특정 기준 날짜를 넘어가면 거절
        # print(replies)
        replyAPI(replies) # day 오늘 날짜
        # for y in hotel[::-1]:
        #     print(y[1:])
        room_assign = makeRoomAssign(present_day)
        data = simulationAPI(room_assign) # 체크인 날짜에 예약이 가능해 승낙을 했던 방만 넣어준다. -> reply 이후에도 정보를 보유하고 있어야 함
        # print(data)
        present_day = data['day']
    print(present_day, scoreAPI())
    print("cancle[amout, N], delay", [cancleM, cancleN], delay)

for i in [1, 2]:
    solution(i)

# 목표
# 객실 수가 많은 예약은 최대한 거절하지 않는다.
# 정확성: 객실 이용률이 목표치와 가까운가
# 효율성: 승낙 / 거절 뭐든 답장을 빨리하면
# 패널티: 승낙했으나 배정 실패 / 거절한 예약의 객실 수 / 거절한 예약의 수

# 호텔
# 한층 - H 층 / W개 객실
# 고유한 객실 번호
    # ABBB
    # AABBB
    # A는 객실 층
    # B는 위치
# 체크아웃 오전 11시 / 체크인 오후 2시 [ 체크 아웃 후 체크인 바로 가능 ]

# 예약
    # id 고유한 6자리 정수
    # 객실 수
    # 체크인 날짜 [ 당일 체크인 요청 없음 ]
    # 체크아웃 날짜

# 객실 배정
# 승인한 예약 -> 체크인 날짜에 호텔 사용 