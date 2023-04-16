S = input()

while( "00" in S):
    S = S.replace("00", "0")
while( "11" in S):
    S = S.replace("11", "1")
print( min(S.count("0"), S.count("1")) )
