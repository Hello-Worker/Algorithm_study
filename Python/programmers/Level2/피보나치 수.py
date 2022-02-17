def solution(n):
    answer = 0
    num = 1
    for i in range(n):
        answer, num = num, answer + num
            
    return answer


