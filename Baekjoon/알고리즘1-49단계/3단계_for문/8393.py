# 3-3) 8393번: 합
n = int(input())
sum = 0  # sum=0으로 초기값을 설정해줘야 sum변수가 생성. 입력하지 않으면 변수선언이 되지않아 런타임 오류발생.
for i in range(n + 1):  # n: n-1까지 포함, n+1:n까지 포함. 문제는 n까지의 합이므로 n+1을 해줘야한다.
    sum += i  # sum = sum+i, i를 반복시키며 sum에 값을 축적.
print(sum)