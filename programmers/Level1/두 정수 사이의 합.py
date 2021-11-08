def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a,b+1):
            answer += i
    else:
        for j in range(b,a+1):
            answer += j
    return answer

#def solution(a, b):
#    return sum(range(min(a,b),max(a,b)+1))