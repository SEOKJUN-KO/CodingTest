# X = 10^6 / cmd = 2*10^6 / n = 10^6
class LinkList:
    def __init__(self):
        self.val = "O"
        self.next = None
        self.pre = None
        self.bridge = None
    

def solution(n, k, cmd):
    answer = ''
    head = LinkList()
    tmp = head
    for i in range(1, n):
        node = LinkList()
        tmp.next = node
        tmp.bridge = node
        node.pre = tmp
        tmp = node
    p = head
    for _ in range(k):
        p = p.next
    st = []
    for c in cmd:
        # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
        if c[0] == "D":
            move = int(c.split(" ")[1])
            for _ in range(move):
                p = p.next
        # "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
        elif c[0] == "U":
            move = int(c.split(" ")[1])
            for _ in range(move):
                p = p.pre
        # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다.
        # 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        elif c[0] == "C":
            p.val = "X"
            st.append(p)
            pp = p.pre
            pn = p.next
            if pp != None:
                pp.next = pn
            if pn != None:
                pn.pre = pp
                p = pn
            else:
                p = pp
        # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
        elif c[0] == "Z":
            node = st.pop()
            node.val = "O"
            pp = node.pre
            pn = node.next
            if pp != None:
                pp.next = node
            if pn != None:
                pn.pre = node
    p = head
    while(p != None):
        answer += p.val
        p = p.bridge
    return answer
