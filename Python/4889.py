import sys

st = sys.stdin.readline().strip()
stack = []
i = 1
ans = 0
while(st[0] != "-" ):
    for c in st:
        if(c == "}"):
            if(stack == []):
                stack.append('{')
                ans += 1
            else:
                stack.pop()
        else:
            stack.append('{')
    print(str(i)+". "+str(ans+(len(stack)//2) ) )
    st = sys.stdin.readline().strip()
    stack = []
    ans = 0
    i += 1
