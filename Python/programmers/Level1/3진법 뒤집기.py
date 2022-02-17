# def solution(n):
#     answer = 0
#     num = []
#     ten = 0
#     s = 0
#     while n>3:
#         if n%3 ==0:
#             num.append(0)
#         else:
#             num.append(int(n%3))
#         n = n//3
#     num.append(int(n))

#     for i in range(len(num)):
#         s = (3**i)*num[len(num)-1-i]
#         ten += s
#         s = 0
#     print(ten)
#     return ten

def solution(n):
    answer = 0
    num = ''
    while(n>=1):
        rest =  n%3
        num = str(rest) + num
        n //= 3

    for i in range(len(num)):
        answer += (3**i)*int(num[i])

    return answer