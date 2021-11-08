def solution(strings, n):
    answer = []
    second = []
    for i in strings:
        second.append(i[n] + i)
    second.sort()
    
    for j in second:
        answer.append(j[1:])
    return answer