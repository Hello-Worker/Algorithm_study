def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        num -= set(range(i*2,n+1,i))
    
    return len(num)