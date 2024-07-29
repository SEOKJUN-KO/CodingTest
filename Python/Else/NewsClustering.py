# https://school.programmers.co.kr/learn/courses/30/lessons/17677
import copy
def solution(str1, str2):
    val = 65536
    if(str1 == "" and str2 == ""): return 65536
    str1, str2 = str1.lower(), str2.lower()
    #97 122
    s1, s2 = {}, {}
    for i in range(len(str1)-1):
        if( 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i+1]) <= 122):
            s1[str1[i:i+2]] = s1.get(str1[i:i+2], 0) + 1
    hop = copy.deepcopy(s1)
    for i in range(len(str2)-1):
        if( 97 <= ord(str2[i]) <= 122 and 97 <= ord(str2[i+1]) <= 122):
            s2[str2[i:i+2]] = s2.get(str2[i:i+2], 0) + 1
            hop[str2[i:i+2]] = max(hop.get(str2[i:i+2], 0), s2[str2[i:i+2]])
    if(s1 == {} and s2 == {}): return val
    elif(s1 == {} or s2 == {}): return 0
    
    gyo = 0
    hopS = 0
    for key in s1.keys():
        gyo += min(s1.get(key, 0), s2.get(key, 0))
    for key in hop.keys():
        hopS += hop[key]
    return int(gyo/hopS*val)
        

    
