def solution(priorities, location):
    answer = 0
    max_num = max(priorities)
    while True:
        for i in range(len(priorities)):
            if max_num == priorities[i]:
                answer += 1
                priorities[i] = 0
                if i == location:
                    return answer
            max_num = max(priorities)
