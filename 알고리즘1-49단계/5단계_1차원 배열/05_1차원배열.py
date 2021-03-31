# 5-1) 10818번: 최소, 최대
N = int(input())
num_list = list(map(int, input().split()))

print(min(num_list), max(num_list), end='')  # 기본 내장함수 사용

# 5-2) 2562번: 최댓값
num_list = []  # num_list라는 빈 리스트를 정의
for i in range(9):  # 9번 반복해서 값을 입력받는다.
    num_list.append(int(input()))  # append는 리스트에 값을 추가하는 함수

print(max(num_list))  # 최댓값을 구하는 함수
print(num_list.index(max(num_list)) + 1)  # index는 0부터시작하고 예제입력에서는 1부터 시작하므로 인덱스에 +1을 해줘야한다.

# 5-3) 2577번: 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
num = A * B * C
num_list = list(str(num))  # num변수 안의 숫자들을 문자열 형식으로 바꿔주고 배열시킴
for i in range(10):  # 0~9까지반복
    print(num_list.count(str(i)))  # i를 문자열로 변환시킨 후 i에 해당하는 문자의 수를 센다.
    # 0~9까지 반복하므로 i의 값은 0~9까지 반복되고, 해당 카운트 값이 출력된다.

# 5-4) 3052번: 나머지
num = []  # 빈 배열 만들어주기
for i in range(10):
    n = int(input())
    num.append(n % 42)  # 입력값을 42로 나눈 나머지들이 num에 저장된다.
print(len(set(num)))  # set은 중복을 제거하고 집합으로 만들어준다.
# 배열에서의 len은 요소의 개수를 출력


# 5-5) 1546번: 평균
N = int(input())  # 과목수
M = list(map(int, input().split()))
M_max = max(M)  # M의 값들 중 최댓값

for i in range(N):  # 과목수 N만큼 반복
    M[i] = M[i] / M_max * 100  # M의 인덱스에 새로운 식 적용
avg = sum(M) / N
print("%.2f" % avg)  # 소수 둘째자리까지 출력

# 5-6) 8958번: OX퀴즈
n = int(input())
for i in range(n):
    a = input()
    jumsu = 0
    sum = 0
    for j in range(len(a)):  # 요소의 개수만큼 반복
        if a[j] == "O":
            jumsu += 1  # O가 연속되면 점수가 1씩 커진다.
            sum += jumsu
        else:
            jumsu = 0  # X가 나오면 jumsu의 값이 0으로 초기화된다.
    print(sum)

# 5-7) 4344번: 평균은 넘겠지
C = int(input())  # 테스트 케이스의 개수
for i in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1:]) / N[0]  # 두번째자리부터 점수가 시작하므로 1:
    cnt = 0
    for j in N[1:]:
        if j > avg:
            cnt += 1
    print('%.3f' % round((cnt / N[0]) * 100, 3) + "%")  # round함수: n번째까지 표현하고 반올림하고 싶을때 사용
