# 5-5) 1546번: 평균
N = int(input()) #과목수
M = list(map(int, input().split()))
M_max = max(M) #M의 값들 중 최댓값

for i in range(N): # 과목수 N만큼 반복
    M[i] = M[i]/M_max*100 # M의 인덱스에 새로운 식 적용
avg = sum(M)/N
print("%.2f" % avg) # 소수 둘째자리까지 출력
