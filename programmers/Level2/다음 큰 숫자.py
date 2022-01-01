def check(x):
    binary = bin(x)
    one = binary.count('1')
    return one
    
def solution(n):
    answer = n
    num = check(n)
    while True:
        answer += 1
        if int(check(answer)) == num:
            return answer

    


