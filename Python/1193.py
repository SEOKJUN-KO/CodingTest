n = int(input())

m = 1
while(n > m):
    if(n - m > 0):
        n -= m
        m += 1
if(m%2 == 1):
    print("%d/%d" %( m-(n-1), 1+(n-1)))
else:
    print("%d/%d" %( 1+(n-1), m-(n-1)))
