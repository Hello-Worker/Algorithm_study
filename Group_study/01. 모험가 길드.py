# N명의 모험가
# 공포도가 X인 모험가는 X명 이상으로 구성한 모험가 그룹에 참여
# 최대 모험가 그룹의 개수
# ex) N=5, 각 각의 공포도가 2 3 1 2 2라면 답은 2

N = map(int,input())
data = list(map(int,input().split()))

data.sort()
cnt = 0
result = 0

for i in data: # 낮은 공포도부터 확인
    cnt += 1
    if cnt >= i : # 인원수가 공포도와 같아지면 그룹 개수 1증가
        result += 1
        cnt = 0

print(result)