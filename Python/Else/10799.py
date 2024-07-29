string = input().strip()

n = 0
s = 0

for i in range(len(string)):
    if(i < len(string) - 1 and string[i:i+2] == "()"):
        s += n
    elif(string[i] == '('):
        n += 1
    elif(string[i] == ')' and string[i-1:i+1] != "()"):
        n -= 1
        s += 1
print(s)
