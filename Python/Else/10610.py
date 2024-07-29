from itertools import permutations

n = list(input())
if('0' not in n):
    print(-1)
    exit()
n = sorted(n)
n = n[::-1]
n = int("".join(n))
if(n%3 == 0):
    print(n)
else:
    print(-1)
