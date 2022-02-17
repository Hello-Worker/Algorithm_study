def solution(s):
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9}

    answer = ''  # 최종문자열
    string = ''

    for i in s:  # 한글자씩 확인
        if i.isdigit():  # 숫자라면
            answer += i
        else:
            string += i  # 하나씩 이어붙이기
            if string in dict.keys():  # 숫자 단어가 되면
                answer += str(dict[string])  # 대응되는 값을 str형태로 붙이기
                string = ''  # 초기화

    return int(answer)
