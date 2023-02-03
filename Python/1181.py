import sys

N = int(sys.stdin.readline())
s = set([])
for _ in range(N):
    s.add(sys.stdin.readline().strip())
ans = sorted(s, key = lambda x: (len(x), x) )

for a in ans:
    print(a)
