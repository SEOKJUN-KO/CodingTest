def solution(files):
    ans = []
    tmpArr = []
    for file in files:
        flag = 0
        tmpS = ""
        tmpA = []
        for i in range(len(file)):
            if flag == 0 and not ( "0" <= file[i] <= "9" ):
                tmpS += file[i]
            elif flag == 0 and ( "0" <= file[i] <= "9" ):
                tmpA.append(tmpS)
                tmpS = file[i]
                flag = 1
            elif flag == 1 and ( "0" <= file[i] <= "9" ):
                tmpS += file[i]
            elif flag == 1 and not ( "0" <= file[i] <= "9" ):
                tmpA.append(tmpS)
                tmpA.append(file[i:])
                tmpS = ""
                break
        if tmpS != "": tmpA.append(tmpS)
        tmpArr.append(tmpA)
    tmpArr.sort(key = lambda x: (x[0].upper(), int(x[1])) )
    for t in tmpArr:
        ans.append("".join(t))
        
    return ans
