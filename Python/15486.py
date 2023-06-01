import sys

input = sys.stdin.readline
N = int(input())
schedule = [[0, 0]]
for _ in range(N):
    schedule.append(list(map(int, input().split())))

DP = [0]*(N+2)
for day in range(N, 0, -1):
    if( day + schedule[day][0] - 1 > N ):
        DP[day] = DP[day+1]
        continue
    DP[day] = max( DP[ day + schedule[day][0] ] + schedule[day][1], DP[ day + 1 ] )
print(DP[1])
