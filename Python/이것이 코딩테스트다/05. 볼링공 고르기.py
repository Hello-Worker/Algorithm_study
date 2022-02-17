# 볼링공 N개, 각 각의 무게가 적혀있음
# 공의 번호는 1번부터 순서대로 부여
# 무게가 같아도 서로 다른공
# 볼링공의 무게는 1부터M까지의 자연수
# 서로 무게가 다른 볼링공을 고르기

import itertools 

N = 5
M = 3
weight = [1,3,2,3,2]
arr = list(itertools.combinations(weight, 2)) # 조합
for i in arr:
    if i[0] == i[1]:
        arr.remove(i) # 같은무게 삭제

print(len(arr))



for i in range(1, m+1)
    n -= array[i]
    result += array[i]*N

[0][1]
