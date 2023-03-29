import sys

n = int(sys.stdin.readline())
s = set([])
for _ in range(n):
    name, situation = sys.stdin.readline().split()
    if(situation=="enter"):
        s.add(name)
    else:
        s.remove(name)
s = sorted(list(s))
s.reverse()
for c in s:
    print(c)
