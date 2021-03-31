# 6-2) 4673_셀프넘버
# https://this-programmer.tistory.com/entry/%EB%B0%B1%EC%A4%804673%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%ED%94%84-%EB%84%98%EB%B2%84 참고
natural_num = set(range(1,10001)) # set함수의 차집합 원리를 이용
generated_num = set()

for i in range(1, 10001): # 12로 예시를 들면 i는 12로 for문 돌림
    for j in str(i): #12를 문자열로받아서(자리대로 분리하기위해) 1,2를 차례대로 반복
        i += int(j) #분리된 1,2를 차례로 받아서 정수로 변환후 i값 12에 더함. 즉, 12+1+2 (생성자로 만들어진 수)
    generated_num.add(i) #set집합 함수에서 원소추가 함수. 생성자로 만들어진 수를 generated_num집합의 원소로 추가.

self_num = sorted(natural_num - generated_num) #차집합. A = 1~10000까지의 수 - 생성자로 만들어진 수

for i in self_num: # sort()는 리스트, sorted()함수는 어떤 리터러블 객체도 받을 수 있음. 정렬 함수.
    print(i) #차집합으로 만들어진 결과집합을 하나씩 출력


