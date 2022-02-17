def gcd(n,m):
    if n < m:
        n,m = m,n
    while(m): #m이 자연수일 때 까지 (True)
        n, m = m, n%m
    return n

def solution(n,m):
    return [gcd(n,m),(n*m)/gcd(n,m)]