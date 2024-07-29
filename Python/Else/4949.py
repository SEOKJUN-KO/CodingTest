import sys

def valance(string):
    stack = []
    for c in string:
        if(c == '(' or c == '['):
            stack.append(c)
        elif(c == ')'):
            if(stack == []): return False
            elif(stack[-1] =='('):
                stack.pop()
            else:
                return False
        elif(c == ']'):
            if(stack == []): return False
            elif(stack[-1] =='['):
                stack.pop()
            else:
                return False
    if(stack == []):
        return True
    else:
        return False

string = sys.stdin.readline()
while(string[:len(string)-1]!="."):
    R = valance(string[:len(string)-1])
    if(R): print("yes")
    else: print("no")
    string = sys.stdin.readline()
