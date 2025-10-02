whoReport = {}
reportedCnt = {}
def doReport(report):
    global whoReport, reportedCnt
    for r in report:
        user, reported = r.split(" ")
        if user not in whoReport.keys():
            whoReport[user] = set()
        whoReport[user].add(reported)
        if reported not in reportedCnt.keys():
            reportedCnt[reported] = set()
        reportedCnt[reported].add(user)

def printAll(id_list, k):
    global whoReport, reportedCnt
    answer = []
    for id in id_list:
        cnt = 0
        if id not in whoReport.keys():
            answer.append(cnt)
            continue
        for reported in whoReport[id]:
            if len(reportedCnt[reported]) >= k:
                cnt += 1
        answer.append(cnt)
    return answer
        
def solution(id_list, report, k):
    doReport(report)
    return printAll(id_list, k)