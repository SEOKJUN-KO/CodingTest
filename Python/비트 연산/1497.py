N, M = map(int, input().split())
arr = []
best = 0

ans = float('inf')
used = []
picked = 0
cnt = 0

def findAll():
    global ans, arr, used, picked, cnt
    
    store = picked
    for i in range(len(arr)):
        if not used[i]:
            picked |= arr[i]
            used[i] = True
            cnt += 1
            if (picked == best):
                ans = min(ans, cnt)
            findAll()
            picked = store
            used[i] = False
            cnt -= 1


for _ in range(N):
    state = 0
    song = input().split()
    song = song[1][::-1]
    for i in range(len(song)):
        if song[i] == "Y":
            state |= ( 1 << i )
    arr.append(state)
    best |= state

if best == 0: print(-1)
else:
    used = [ False for _ in range(N) ]
    findAll()
    print(ans)
    