# 5-3) 2577번: 숫자의 개수
A = int(input())
B = int(input())
C = int(input())

num = A*B*C
num_list = list(str(num)) #num변수 안의 숫자들을 문자열 형식으로 바꿔주고 배열시킴
for i in range(10): #0~9까지반복
    print(num_list.count(str(i))) #i를 문자열로 변환시킨 후 i에 해당하는 문자의 수를 센다.
                                  #0~9까지 반복하므로 i의 값은 0~9까지 반복되고, 해당 카운트 값이 출력된다.