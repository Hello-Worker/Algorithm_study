# 2-1) 1330번: 두 수 비교하기
A,B = input().split()
A = int(A)
B = int(B)
if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')