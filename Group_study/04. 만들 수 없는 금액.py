# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값
# ex) N = 3, 동전이 각 각 3,5,7이면 만들 수 없는 최솟값은 1원
# 첫째 줄에 동전 개수N
# 둘째 줄에 동전의 화폐 단위 주어짐
# 최솟값 출력하라

# from itertools import combinations
# import itertools

# N = 5
# data = [3,2,1,1,9]

# data2 = [] # 동전으로 만들 수 있는 경우의 수
# for i in data:
#     com = itertools.combinations(data, i)
#     data.append(com)

# print(data2)

n = 5
coin = [1, 2, 3, 8]
coin.sort()
target = 1
for c in coin:
    if c <= target:
        target+=c
    else:
        break
print(target)