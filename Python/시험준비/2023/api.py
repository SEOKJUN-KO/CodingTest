import requests

base_url = "https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api/"
auth_key = ""
def startAPI(n):
    global base_url, auth_key
    headers = {
        "X-Auth-Token": "6e2f8e97ab94614f34a24202",
        "Content-Type": "application/json"
    }

    json = { "problem": n }
    try:
        res = requests.post(url=base_url+"/start", headers=headers, json=json)
        res.raise_for_status()
        data = res.json()
        auth_key = data["auth_key"]
    except:
        print("startAPI error")
    
def get(end, methodName):
    global base_url, auth_key
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    try:
        res = requests.get(url=base_url+end, headers=headers)
        res.raise_for_status()
        data = res.json()
        return data
    except:
        print(methodName + " error")

def put(end, json, methodName):
    global base_url, auth_key
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }
    try:
        res = requests.put(url=base_url+end, headers=headers, json=json)
        res.raise_for_status()
        data = res.json()
        return data
    except:
        print(methodName + " error")

# 현재 날짜에 새로 들어온 예약 요청의 정보를 반환
def newRequestAPI():
    data = get("/new_requests", "newRequestAPI")
    return data['reservations_info']

# 특정 예약 요청에 대한 승낙 / 거절을 답변
def replyAPI(replies):
    json = {
        "replies": replies
    }
    data = put("/reply", json, "replyAPI")
    return data['day']

# 오늘 호텔에 체크인 하려는 손님들에게 객실 번호를 배정해 서버에 전달하고 1일이 진행됩니다.

# 응시자에게 전달받은 순서대로 객실을 배정합니다.
    # (전달받은 객실 번호) ~ (전달받은 객실 번호 + 객실 수 - 1)의 객실을 손님에게 배정합니다.
    # 만약 객실이 비어있지 않거나 객실 번호의 범위가 올바르지 않다면 무시합니다.
    # 객실을 성공적으로 배정했다면 해당 객실들은 체크아웃 날짜 전까지 사용 중인 상태가 됩니다.
# 호텔에 도착한 손님 중 객실이 배정되지 않은 손님은 객실 배정에 실패한 것으로 처리됩니다.
# 답변하지 않은 예약 중 답변 기한이 현재 날짜인 예약은 거절한 것으로 처리됩니다.
# 현재 날짜가 1일 증가합니다.
# 현재 날짜에 체크아웃하는 객실들이 빈 객실이 됩니다.
# 현재 날짜에 체크인하는 손님들이 호텔에 도착합니다.
def simulationAPI(room_assign):
    json = {
        "room_assign": room_assign
    }
    data = put("/simulate", json, "simulationAPI")
    return data # day: 1일 뒤 날짜 # fail_count: 응시자가 예약을 승낙했으나 실패한 횟수


def scoreAPI():
    data = get("/score", "scoreAPI")
    return data