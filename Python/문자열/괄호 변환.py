# p = 1000
# 균형잡힌 괄호 문자열 = ( ) 개수 맞을 때
# 올바른 괄호 문자열
def isCorrect(u):
    st = []
    for c in u:
        if c == "(":
            st.append("(")
        else:
            if st != [] and st[-1] == "(":
                st.pop()
            else:
                st.append(")")
                break
    if st == []: return True
    return False

def backFlip(u):
    q = list(u[1:len(u)-1])
    for i in range(len(q)):
        if q[i] == ")": q[i] = "("
        else: q[i] = ")"
    return "".join(q)

def second(w):
    l, r, idx = 0, 0, 0
    for i in range(len(w)):
        if w[i] == "(": l += 1
        else: r += 1
        if l == r:
            idx = i
            break
    u = w[:idx+1]
    
    u = w[:idx+1]
    v = w[idx+1:]
    if isCorrect(u):
        return u + solution(v)
    else:
        return "("+solution(v)+")"+backFlip(u)
    
def solution(p):
    ans = p
    if isCorrect(ans) or ans == "": return ans
    return second(ans)
