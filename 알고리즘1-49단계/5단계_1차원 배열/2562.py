# 5-2) 2562번: 최댓값
num_list = [] #num_list라는 빈 리스트를 정의
for i in range(9): # 9번 반복해서 값을 입력받는다.
    num_list.append(int(input())) # append는 리스트에 값을 추가하는 함수

print(max(num_list)) #최댓값을 구하는 함수
print(num_list.index(max(num_list))+1) #index는 0부터시작하고 예제입력에서는 1부터 시작하므로 인덱스에 +1을 해줘야한다.