# 3-1) 2739번: 구구단
N = int(input())  # 정수로 수를 받아줌.
for i in range(1, 10):  # 1부터 9까지 i를 반복
    print("%d * %d = %d" % (N, i, N * i))  # %d: 정수형, %s: 문자열