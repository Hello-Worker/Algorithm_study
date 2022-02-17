def solution(x, n):
    answer = []
    for i in range(1,n+1):
        sol = x*i
        answer.append(sol)
    return answer