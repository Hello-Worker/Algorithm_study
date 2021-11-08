def solution(a, b):
    answer = ''
    day = 0
    days = ['THU','FRI', 'SAT','SUN', 'MON', 'TUE', 'WED']
    month = ['31', '29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
    for i in range(a-1):
        day += int(month[i])
    day += b
    answer += days[(day % 7)]
        
    return answer