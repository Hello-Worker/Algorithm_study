def solution(s, n):
    answer = ''
    trans = 0
    for i in s:
        trans += ord(i) + int(n)
        if ord(i) == 32:
            answer += chr(32)

        elif 64<ord(i)<91:
            if trans>90:
                answer += chr(trans-26)
            else:
                answer += chr(trans)
        elif 96<ord(i):
            if trans > 122:
                answer += chr(trans-26)
            else:
                answer += chr(trans)
        trans = 0
    return answer

