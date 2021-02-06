# 5-4) 3052번: 나머지
num = [] #빈 배열 만들어주기
for i in range(10):
    n = int(input())
    num.append(n%42) #입력값을 42로 나눈 나머지들이 num에 저장된다.
print(len(set(num))) #set은 중복을 제거하고 집합으로 만들어준다.
                     #배열에서의 len은 요소의 개수를 출력