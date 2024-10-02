# 같은 [A->B] 중복 1회로 처리
# k 번 이상 신고된 유저 -> 메일 발송
def solution(id_list, report_list, k):
    reportD = {}
    reportedD = {}
    ans = []
    for id in id_list:
        reportD[id] = set([])
        reportedD[id] = 0
    for r in report_list:
        report, reported = r.split(" ")
        if reported not in reportD[report]:
            reportD[report].add(reported)
            reportedD[reported] += 1
    for id in id_list:
        cnt = 0
        for reported in reportD[id]:
            if reportedD[reported] >= k: cnt += 1
        ans.append(cnt)
    return ans
