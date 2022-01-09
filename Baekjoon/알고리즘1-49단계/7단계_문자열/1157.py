# 7-5) 1157_단어 공부
a = input().upper() #대문자로 변환
a_list = list(set(a)) #입력받은 문자열에서 중복값 제거 후 리스트화
t = [] #알파벳 개수를 저장할 list
for i in a_list:
    t.append(a.count(i)) #a_list에서 i 개수 카운트 후 해당 값을 t에 추가

if t.count(max(t)) >= 2: #최대값의 개수를 카운트
    print("?")
else:
    print(a_list[(t.index(max(t)))].upper()) #t에서 t의 최대값이 있는 인덱스번호 찾기. 후에 대문자로 변환하여 출력.