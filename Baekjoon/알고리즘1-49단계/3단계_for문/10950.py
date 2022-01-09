# 3-2) 10950번: A+B-3
T = int(input())
for i in range(T):  # 0부터 시작이므로 T-1까지 T회 반복. T+1안해줘도 됨.
    A, B = input().split()  # 문자열로 받은 후 split()공백을 기준으로 두 수를 나눠준다.
    A = int(A)  # A 정수형으로
    B = int(B)  # B 정수형으로
    print(A + B)