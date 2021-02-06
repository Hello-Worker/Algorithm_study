# 2-1) 1330번: 두 수 비교하기
A, B = input().split()
A = int(A)
B = int(B)
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# 2-2) 9498번: 시험 성적
a = input()
a = int(a)
if 90 <= a:
    print("A")
elif 80 <= a:
    print("B")
elif 70 <= a:
    print("C")
elif 60 <= a:
    print("D")
else:
    print("F")

# 2-3) 2753번: 윤년
a = input()
a = int(a)
if a % 4 == 0 and a % 100 != 0:
    print('1')
elif a % 4 == 0 and a % 400 == 0:
    print('1')
else:
    print('0')

# 2-4) 14681번: 사분면 고르기
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')

# 2-5) 2884번: 알람 시계
a, b = input().split()
a = int(a)
b = int(b)
if b >= 45:
    print(a, b - 45)
elif a > 0 and b < 45:
    sol = b + 15
    print(a - 1, sol)
else:
    sol = b + 15
    print("23", sol)
