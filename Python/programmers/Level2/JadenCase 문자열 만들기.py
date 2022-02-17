

def solution(s):
    answer = ''
    lists = s.split(' ')
    for i in lists:
        answer += i.capitalize()
        answer += ' '
        
    return answer[:-1]
