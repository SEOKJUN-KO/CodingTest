from collections import deque

def solution(cards):
    ans = 0
    que = deque()
    arr = [0]
    for i in range(len(cards)):
        if cards[i] != 0:
            cnt = 1
            que.append(cards[i]-1)
            cards[i] = 0
            while(que):
                now = que.popleft()
                if cards[now] != 0:
                    que.append(cards[now]-1)
                    cards[now] = 0
                    cnt += 1
            arr.append(cnt)
    arr = sorted(arr)
    return arr[-1]*arr[-2]