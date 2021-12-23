from itertools import permutations

def test(num):
    if num < 2:
        return False
    
    for k in range(2,num):
        if num % k == 0:
            return False

    return True
        

def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        per = list(map(''.join,permutations(numbers,i)))
        for j in list(set(per)):
            if test(int(j)):
                answer.append(int(j))
                
    return len(set(answer))
