# 5-6) 8958번: OX퀴즈
n = int(input())
for i in range(n):
    a = input()
    jumsu = 0
    sum = 0
    for j in range(len(a)): #요소의 개수만큼 반복
        if a[j] == "O":
            jumsu += 1 #O가 연속되면 점수가 1씩 커진다.
            sum += jumsu
        else:
            jumsu = 0 #X가 나오면 jumsu의 값이 0으로 초기화된다.
    print(sum)







