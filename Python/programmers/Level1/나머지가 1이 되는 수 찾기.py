def solution(n):
    i = 1
    while n>=1:
        if n%i == 1:
            return i
        else:
            i+=1