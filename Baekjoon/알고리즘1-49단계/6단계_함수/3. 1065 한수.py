# 6-3) 1065_한수

num = int(input())
hansu = 0

for i in range(1, num+1): #num까지 포함
    if i <= 99: # 1부터 99까지는 모두 함수
        hansu += 1

    else:
        nums = list(map(int, str(i))) #숫자를 자릿수대로 분리(리스트화)
        if nums[0] - nums[1] == nums[1] - nums[2]: #등차수열 조건
            hansu+=1
print(hansu)