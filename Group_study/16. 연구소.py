# 3개의 벽 세울 수 있음
# 최대 안전 구역 확보 : 2가 가장 min인 경우


# 입력받기
n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 2의 위치 찾기
where2 = []
for i in range(n):
    for j in range(m):
        if data[i][j]==2:
            where2.append([i,j])

print(where2)
