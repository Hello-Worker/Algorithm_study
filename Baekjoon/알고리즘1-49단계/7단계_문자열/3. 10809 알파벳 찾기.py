# 7-3) 10809번: 알파벳 찾기
word = input()
alphabet = list(range(97,123)) #아스키코드 숫자 범위를 리스트 변환
for i in alphabet:
    print(word.find(chr(i)), end=" ") # chr()함수는 숫자(아스키코드)를 문자로 변환하는 함수
                             # 문자->숫자(아스키코드) 변환함수는 ord()
                             # find 함수는 문자열에서만 사용 가능한 함수. 문자가 문자열안에 포함되지 않을 경우 -1 출력(index는 에러)


