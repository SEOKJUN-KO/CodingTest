n = int(input())
f = n//5

while(f >= 0):
    k = n
    k -= 5*f
    if(k%3 == 0):
        print(f+k//3)
        exit()
    f -= 1
print(-1)
