def solution(s):
    answer = ''
    cnt = len(s) // 2
    if len(s)%2 == 0:
        answer += s[cnt-1]
        answer += s[cnt]
    else:
        answer += s[cnt]
    return answer