def solution(price, money, count):
    pay = 0
    for i in range(1,count+1):
        pay += i*price
    return abs(money-pay) if pay>money else 0