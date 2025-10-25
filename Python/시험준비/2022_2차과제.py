import requests

BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

def startAPI(n):
    url = BASE_URL+"/start"
    headers = {
        "X-Auth-Token": "9dcd055b3b3c447caaa27e92",
        "Content-Type": "application/json"
    }
    json = {
        "problem": n
    }
    try:
        res = requests.post(url=url, headers=headers, json=json)
        res.raise_for_status()
        data = res.json()
        return data['auth_key']
    except:
        print("startAPI error")

# 현재 대기열에서 매칭을 대기 중인 유저들의 정보를 반환
def waitingLineAPI(auth_key):
    url = BASE_URL+"/waiting_line"
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    try:
        res = requests.get(url=url, headers=headers)
        res.raise_for_status()
        data = res.json()
        return data['waiting_line']
    except:
        print("waitingLineAPI error")

# 이번 턴에 게임이 끝난 유저들의 게임 결과를 반환한다.
def gameResultAPI(auth_key):
    url = BASE_URL+"/game_result"
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    try:
        res = requests.get(url=url, headers=headers)
        res.raise_for_status()
        data = res.json()
        return data['game_result']
    except:
        print("gameResultAPI error")

# 유저
# 고유 id (1 ~ ) / 고유 실력 1000 ~ 100000 / 같은 실력인 사람 없음
# 시나리오 2. 어뷰져
# 모든 유저들의 현재 등급을 반환
def userInfoAPI(auth_key):
    url = BASE_URL+"/user_info"
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    try:
        res = requests.get(url=url, headers=headers)
        res.raise_for_status()
        data = res.json()
        return data['user_info']
    except:
        print("userInfoAPI error")

def changeGradeAPI(auth_key, commands):
    url = BASE_URL+"/change_grade"
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    json = {
        "commands": commands
    }
    try:
        res = requests.put(url=url, headers=headers, json=json)
        res.raise_for_status()
        return
    except:
        print("changeGradeAPI error")

# 게임 매칭
# 매칭 신청 -> 대기열 [ 15분까지 기다리고, 초과 시 대기열에서 제외]
# 매칭 취소 후 곧바로 매칭 신청 가능
# 1) 너무 오래 기다리지 않게
# 2) 공정하게 등급을 받게
    # 고유 실력 등수와 등급 등수가 비슷하게 매칭을 성사시키자
# 매칭에 성공하면, 대기열에서 제거한다.

# 매칭할 유저의 쌍을 배열에 담아 서버에 전달
def matchAPI(auth_key, pairs):
    url = BASE_URL+"/match"
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    json = {
        "pairs": pairs
    }

    try:
        res = requests.put(url=url, headers=headers, json=json)
        res.raise_for_status()
        data = res.json()
        return data
    except:
        print("matchAPI error")

# 시간 고려 안한 매칭 / 3 등급 이내의 차이만 매칭
userDict = {}
def matching(auth_key, waiting_line, time):
    global userDict
    pairs = []
    used = set()
    for waiting in waiting_line:
        id, fromT = waiting['id'], waiting['from']
        grade = userDict[id].grade
        if id in used: continue

        for other in waiting_line:
            oId, oFromT = other['id'], other['from']
            oGrade = userDict[oId].grade
            if oId in used: continue
            if oId == id: continue

            if abs(grade-oGrade) <= 3:
                used.add(id)
                used.add(oId)
                pairs.append([id, oId])

    return matchAPI(auth_key, pairs)


# 게임

# 이길 확률 = ( A의 고유 실력 ) / ( A 고유실력 + B 고유실력 ) 
# 걸리는 시간 = 40분 - ( 두 유저간 고유 실력 차 / 99000 * 35 ) + e [ -5 ~ 5 인 무작위 정수 값 ] ( 버림 -> 정수 ) [v]
    # -> 3분보다 작으면 3 / 40분 보다 크면 40
# => 실력이 차이가 높으면, 이길 확률 높아지고, 걸리는 시간은 작아진다. 
def translate(A):
    return A//9
    
def getWeight(taken):
    A = 90000
    if taken < 8: return translate(A)
    while(A > 0):
        B = int(40 - ( A / 99000 * 35 ))
        if B == taken: break 
        if not ( 3 <= B <= 40 ): break
        if B > taken: A += 7 # 예상 걸리는 시간이 큼 => 예상 실력 차이가 작음
        elif B < taken: A -= 7 # 예상 걸리는 시간이 걸린 시간보다 => 예상 실력차이가 큼
    return translate(A)

def changeGrade(auth_key, game_result):
    global userDict
    commands = []
    for game in game_result:
        win_id, lose_id, taken = game['win'], game['lose'], game['taken']
        weight = (getWeight(taken))//2
        winner = userDict[win_id]
        # 등급은 0 이상 9999 이하        
        if winner.grade < 9999:
            win_grade = winner.grade+weight
            if win_grade > 9999: win_grade = 9999
            commands.append({"id": win_id, "grade": win_grade})
            winner.change(win_grade)
        
        loser = userDict[lose_id]
        if loser.grade > 0:
            lose_grade = loser.grade-weight
            if lose_grade < 0: lose_grade = 0
            commands.append({"id": lose_id, "grade": lose_grade})
            loser.change(lose_grade)
    changeGradeAPI(auth_key, commands)
    return

class User:
    def __init__(self, grade):
        self.grade = grade

    def change(self, grade):
        self.grade = grade

def initUserInfo(user_info):
    global userDict
    for user in user_info:
        id, grade = user['id'], user['grade']
        userDict[id] = User(grade)

def scoreAPI(auth_key):
    url = BASE_URL+"/score"
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    try:
        res = requests.get(url=url, headers=headers)
        res.raise_for_status()
        return res.json()
    except:
        print("scoreAPI error")
    return

def solution():
    auth_key = startAPI(1)

    user_info = userInfoAPI(auth_key)
    initUserInfo(user_info)

    matchAPI(auth_key, [])
    # 매칭 받는 시간 1분 ~ 540분
    # 게임 결과 볼 수 있는 시간 1분 ~ 595분
    for t in range(1, 596):
        game_result = gameResultAPI(auth_key)
        if game_result != []:
            changeGrade(auth_key, game_result)
        if 1 <= t <= 540:
            waiting_line = waitingLineAPI(auth_key)
            print(matching(auth_key, waiting_line, t), flush=True)
        else:
            matchAPI(auth_key, [])
    print(scoreAPI(auth_key))
solution()

# Start API
# WaitingLine API: 현재 대기열에서 매칭을 대기 중인 유저들의 정보 반환 [v]
# GameResult API: 이번 턴에 게임이 끝난 유저들의 게임 결과를 반환 [v]
# UserInfo API: 모든 유저들의 현재 등급을 반환한다. [v]
# Match API: 매칭하여 게임을 시작 [v]
# ChangeGrade API: 유저의 등급을 수정 [v]