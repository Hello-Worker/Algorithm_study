#5-7) 4344번: 평균은 넘겠지
C = int(input()) #테스트 케이스의 개수
for i in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1:])/N[0] #두번째자리부터 점수가 시작하므로 1:
    cnt = 0
    for j in N[1:]:
        if j>avg:
            cnt += 1
    print('%.3f' % round((cnt/N[0])*100,3)+"%")#round함수: n번째까지 표현하고 반올림하고 싶을때 사용

