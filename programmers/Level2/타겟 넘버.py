from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    
    while queue:
        n, i = queue.popleft()
        
        if i < len(numbers)-1:
            i += 1
            queue.append([n+numbers[i], i])
            queue.append([n-numbers[i], i])
            
        else:
            if n == target:
                answer += 1
                
    return answer