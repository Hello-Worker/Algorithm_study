# 7-4) 2675_문자열 반복
T = int(input())
for i in range(T):
    num, S = input().split() #공백을 기준으로 입력받은 값을 분리.
    text = ''
    for j in S:
        text += int(num)*j
    print(text)

