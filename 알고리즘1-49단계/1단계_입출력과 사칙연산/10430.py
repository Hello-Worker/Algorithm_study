# 1-10) 10430번: 나머지
A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A+B)%C)
print((A%C+B%C)%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)