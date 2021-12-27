def solution(arr):
    arr.sort()
    m = arr[-1]
    answer = m
    while True:
        for i in range(len(arr)-1):
            if answer % arr[i] != 0:
                break
        else:
            return answer
        answer += m

solution([2,6,8,14])