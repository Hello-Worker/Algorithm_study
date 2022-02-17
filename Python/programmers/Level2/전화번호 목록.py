def solution(phone_book):
    answer = True
    dic = {}
    for k in phone_book:
        dic[k] = 1
        
    for number in phone_book:
        temp =''
        for num in number:
            temp += num
            if temp in dic and temp != number:
                answer = False
    return answer