# 2-5) 2884번: 알람 시계
a,b = input().split()
a = int(a)
b = int(b)
if b>=45:
    print(a,b-45)
elif a>0 and b<45:
    sol = b+15
    print(a-1,sol)
else:
    sol = b+15
    print("23",sol)