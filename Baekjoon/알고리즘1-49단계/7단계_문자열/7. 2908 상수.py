# 7-7) 2908_상수
a, b = input().split()

a = int(a[::-1]) #리스트 거꾸로 출력
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
