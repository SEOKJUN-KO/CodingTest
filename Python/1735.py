import math

A, B = map(int, input().split())
C, D = map(int, input().split())

A = A*D+C*B
B = B*D

C = math.gcd(A, B)
print(A//C, B//C)
