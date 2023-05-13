import math
n = int(input())
s = str(math.factorial(n))
if(n == 0 or s[-1] != "0"):
    print(0)
    exit()
ans = 0
for c in s[::-1]:
    if(c != "0"):
        break
    ans += 1
print(ans)
