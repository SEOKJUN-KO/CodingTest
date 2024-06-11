# 아이디 규칙 맞는지 확인
# 아이디 규칙에 맞이 않는다면 유사한 아이디 추천
# 길이 3 - 15
# 소문자, 숫자, -, _, .[ 처음과 끝 사용 불가, 연속 사용 불가 ]

def solution(new_id):
    ans = list(new_id)
    for i in range(len(ans)):
        if not ans[i].isdigit():
            ans[i] = ans[i].lower()
            n = ord(ans[i])
            if not ( 97 <= n <= 122 or n == 45 or n == 46 or n == 95 ):
                ans[i] = ""
    ans = "".join(ans)
    while(".." in ans):
        ans = ans.replace("..", ".")
    if ans != "" and ans[0] == ".":
        ans = ans[1:]
    if ans != "" and ans[-1] == ".":
        ans = ans[:len(ans)-1]
    if ans == "": ans += "a"
    ans = ans[:15]
    if ans != "" and ans[-1] == ".":
        ans = ans[:len(ans)-1]
    while(len(ans) < 3):
        ans += ans[-1]
    return ans
