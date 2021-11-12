def solution(n):
    answer = []
    m = reversed(str(n))
    for i in m:
        answer.append(int(i))
    return answer