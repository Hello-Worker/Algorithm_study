def solution(n):
    num = str(n)
    return int(''.join(sorted(num,reverse=True)))