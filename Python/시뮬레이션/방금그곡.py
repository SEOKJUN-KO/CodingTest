# 재생된 시간 긴 음악, 먼저 입력된 음악 제목 순
# else (None)
dic = {"A#": "H", "C#": "I", "D#": "J", "F#": "K", "G#": "L", "E#": "M", "B#": "O"}
def makeArr(st):
    notesArr = []
    i = 0
    while(i < len(st)):
        if i+1 < len(st):
            if st[i+1] == "#":
                notesArr.append(dic[st[i]+st[i+1]])
                i = i+2
            else:
                notesArr.append(st[i])
                i = i+1
        else:
            notesArr.append(st[i])
            i = i+1
    return notesArr

def solution(m, musicinfos):
    musicinfos = musicinfos
    m = "".join(makeArr(m))
    for j in range(len(musicinfos)):
        start, end, title, notes = musicinfos[j].split(",")
        musicinfos[j] = [start, end, title, makeArr(notes)]
    ans = [0, '']
    for start, end, title, notesArr in musicinfos:
        st = end.split(":")
        endTime = int(st[0])*60 + int(st[1])
        st = start.split(":")
        startTime = int(st[0])*60 + int(st[1])
        q = (endTime-startTime)//len(notesArr) + 1
        notesArr = notesArr*q
        if m in "".join(notesArr[:endTime-startTime]):
            if ans[0] < endTime-startTime:
                ans = [endTime-startTime, title]
    if ans[0] != 0: return ans[1]
    else: return "(None)"
