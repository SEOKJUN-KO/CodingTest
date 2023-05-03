s = input()
i = 0
flag = 0
flag2 = 0
while(i< len(s)):
    if( flag2 == 0 and s[i] == '0' ):
        s = s[:i]+s[i+1:]
        continue
    if( flag2 == 0 and s[i] != '0' ):
        flag2 = 1
    if(s[i] == '+' or s[i] == '-'):
        flag2 = 0
    if(s[i] == '-' and flag == 0):
        s = s[:i+1]+'('+s[i+1:]
        flag = 1
        i += 2
    elif(s[i] == '-' and flag == 1):
        s = s[:i]+')'+s[i:]
        flag = 0
        i += 1
    else:
        i+=1
if(flag == 1):
    s = s+')'
print(eval(s))
