# 3-1) 구구단
N = int(input())  # 정수로 수를 받아줌.
for i in range(1, 10):  # 1부터 9까지 i를 반복
    print("%d * %d = %d" % (N, i, N * 1))  # %d: 정수형, %s: 문자열

# 3-2) A+B - 3
T = int(input())
for i in range(T):  # 0부터 시작이므로 T-1까지 T회 반복. T+1안해줘도 됨.
    A, B = input().split()  # 문자열로 받은 후 split()공백을 기준으로 두 수를 나눠준다.
    A = int(A)  # A 정수형으로
    B = int(B)  # B 정수형으로
    print(A + B)

# 3-3) 합
n = int(input())
sum = 0  # sum=0으로 초기값을 설정해줘야 sum변수가 생성. 입력하지 않으면 변수선언이 되지않아 런타임 오류발생.
for i in range(n + 1):  # n: n-1까지 포함, n+1:n까지 포함. 문제는 n까지의 합이므로 n+1을 해줘야한다.
    sum += i  # sum = sum+i, i를 반복시키며 sum에 값을 축적.

print(sum)

# 3-4) 빠른 A+B
import sys

T = int(input())  # input은 속도가 느려 여러개 입력시 sys를 import한 후 해당 함수를 사용.
# sys.stdin.readline() : 한 라인 입력 받을 떄
# sys.stdin() : 여러 줄 입력 받을 때
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# 3-5) N 찍기
N = int(input())
for i in range(1, N + 1):
    print(i)

# 3-6) 기찍 N
N = int(input())
for i in range(N, 0, -1):  # N부터 0까지 -1증감.
    print(i)

# 3-7) A+B -7
import sys

T = int(input())
for i in range(1, T + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" % (i, a + b))

# 3-8) A+B -8
import sys

T = int(input())
for i in range(1, T + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i, a, b, a + b))

# 3-9) 별 찍기-1
N = int(input())
for i in range(1, N + 1):
    print("*" * i)

# 3-10) 별 찍기-2
N = int(input())
for i in range(N):
    i += 1
    print(" " * (N - i) + "*" * i)

# 3-11) x보다 작은 수
import sys

N, X = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))  # list로 각 숫자에 인덱스 부여
for i in A:
    if i < X:
        print(i, end=" ")  # end=" " 공백으로 띄울 것

