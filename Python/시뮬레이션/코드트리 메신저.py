import sys; input = sys.stdin.readline
from copy import deepcopy
# 100 사내 메신저 준비
# 0 ~ N 채팅방
# 0 이외의 모든 채팅방은 부모 채팅방 존재
# 부모의 번호가 배열로 들어옴
# 신호 발신, 권한 세기만큼 부모로 올라감
class Room:
    def __init__(self, uuid, power):
        self.uuid = uuid
        self.power = power
        self.setting = True
        self.parent = None
        self.left = None
        self.right = None
        self.signals = {}
        self.signals[power] = 1
        self.cnt = 1

arr = []

def calculateAll(uuid):
    global arr
    room = arr[uuid]
    for child in [room.left, room.right]:
        if child == None: continue
        ret = calculateAll(child.uuid)
        for key in ret.keys():
            if key-1 < 0: continue
            if key-1 not in room.signals.keys(): room.signals[key-1] = 0
            room.signals[key-1] += ret[key]
            room.cnt += ret[key]
            if room.signals[key-1] == 0: del(room.signals[key-1])
    return room.signals

def ready(parents, powers):
    global arr
    arr.append(Room(0, 0))
    for i in range(len(powers)): arr.append(Room(i+1, powers[i]))
    for i in range(len(parents)):
        arr[i+1].parent = arr[parents[i]]
        if arr[parents[i]].left == None: arr[parents[i]].left = arr[i+1]
        else: arr[parents[i]].right = arr[i+1]
    calculateAll(0)

# 200 알림망 설정
# 온 <-> 오프
# OFF: 자기자신에서 올라가는 신호는 자름
def toggleSetting(c):
    global arr
    room = arr[c]
    room.setting = not room.setting
    
    parent = room.parent; up = 1
    tmp = deepcopy(room.signals)
    while(parent != None):
        tmpkey = []
        for key in tmp.keys():
            if key-up < 0: tmpkey.append(key); continue
            if room.setting:
                if key-up not in parent.signals.keys(): parent.signals[key-up] = 0
                parent.signals[key-up] += tmp[key]
                parent.cnt += tmp[key]
            else:
                if key-up not in parent.signals.keys(): continue
                parent.signals[key-up] -= tmp[key]
                parent.cnt -= tmp[key]
            if parent.signals[key-up] == 0: del(parent.signals[key-up])
        for t in tmpkey: del(tmp[t])
        if not parent.setting: return
        parent = parent.parent; up += 1

# 300 권한 세기 변경
def changePower(c, power):
    global arr
    room = arr[c]
    if room.power == power: return
    exP = room.power
    room.signals[exP] -= 1
    if room.signals[exP] == 0: del(room.signals[exP])
    if power not in room.signals.keys(): room.signals[power] = 0
    room.signals[power] += 1; room.power = power
    if not room.setting: return

    parent = room.parent; up = 1
    while(parent != None):
        if exP-up < 0 and power-up < 0: return
        if exP-up >= 0:
            parent.signals[exP-up] -= 1; parent.cnt -= 1
            if parent.signals[exP-up] == 0: del(parent.signals[exP-up])

        if power-up >= 0:
            if power-up not in parent.signals.keys(): parent.signals[power-up] = 0
            parent.signals[power-up] += 1; parent.cnt += 1

        if not parent.setting: return
        parent = parent.parent; up += 1

# 400 자리바꾸기
# 자기 자신 포함, 서브 트리까지 옮김
def changeRoom(c1, c2):
    global arr
    room1 = arr[c1]
    room2 = arr[c2]
    # 삭제
    for room in [room1, room2]:
        if not room.setting: continue
        parent = room.parent; up = 1
        tmp = deepcopy(room.signals)
        while(parent != None):
            tmpkey = []
            for key in tmp.keys():
                if key-up < 0: tmpkey.append(key); continue
                parent.signals[key-up] -= tmp[key]
                parent.cnt -= tmp[key]
                if parent.signals[key-up] == 0: del(parent.signals[key-up])
            for t in tmpkey: del(tmp[t])
            if len(tmp) == 0: break
            if not parent.setting: break
            parent = parent.parent; up += 1
    # 교환
    if room1.parent.left == room1: room1.parent.left = room2
    else: room1.parent.right = room2
    if room2.parent.left == room2: room2.parent.left = room1
    else: room2.parent.right = room1
    (room1.parent, room2.parent) = (room2.parent, room1.parent)

    # 추가
    for room in [room1, room2]:
        if not room.setting: continue
        parent = room.parent; up = 1
        tmp = deepcopy(room.signals)
        while(parent != None):
            tmpkey = []
            for key in tmp.keys():
                if key-up < 0: tmpkey.append(key); continue
                if key-up not in parent.signals.keys(): parent.signals[key-up] = 0
                parent.signals[key-up] += tmp[key]
                parent.cnt += tmp[key]
            for t in tmpkey: del(tmp[t])
            if len(tmp.keys()) == 0: break
            if not parent.setting: break
            parent = parent.parent; up += 1

# 500 채팅방 수 조회 -> 카운트 안하게, 미리 계산하기
# 해당 채팅방까지 알림을 쏠 수 있는 채팅방 수
# 미리 계산이 되어있는 상태여야한다.
def countRoom(c):
    global arr
    room = arr[c]
    cnt = 0
    print(room.cnt-1)

def init():
    N, Q = map(int, input().split(" "))
    for _ in range(Q):
        line = list(map(int, input().split(" ")))
        if line[0] == 100:
            parents, powers = line[1:N+1], line[N+1:]
            ready(parents, powers)
        elif line[0] == 200:
            toggleSetting(line[1])
        elif line[0] == 300:
            changePower(line[1], line[2])
        elif line[0] == 400:
            changeRoom(line[1], line[2])
        elif line[0] == 500:
            countRoom(line[1])

init()
