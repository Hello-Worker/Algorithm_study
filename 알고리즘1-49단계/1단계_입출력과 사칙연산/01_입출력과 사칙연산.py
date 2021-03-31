# 1-1) 2557번: Hello World
print("Hello World!")

# 1-2) 10718번: We love kriii
print("강한친구 대한육군")
print("강한친구 대한육군")

# 1-3) 10171번: 고양이
print('\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')

# 1-4) 10172번: 개 (틀림)
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\__|')

# 1-5) 1000번: A+B
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)

# 1-6) 1001번: A-B
a,b = input().split()
print(int(a)-int(b))

# 1-7) 10998번: AXB
a,b = input().split()
print(int(a)*int(b))

# 1-8) 1008번: A/B
a,b = input().split()
print(int(a)/int(b))

# 1-9) 10869번: 사칙연산
A,B = input().split()
A = int(A)
B = int(B)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# 1-10) 10430번: 나머지
A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A+B)%C)
print((A%C+B%C)%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 1-11) 2588번: 곱셈
A= int(input())
B= input()
a = A*int(B[2])
b = A*int(B[1])
c = A*int(B[0])
d = A* int(B)
print(a, b, c, d, sep='\n')