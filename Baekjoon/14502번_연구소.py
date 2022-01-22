# 1. 벽을 임의로 3개 세우는 모든 경우의 수 구함.
# 2. 바이러스를 흩뿌린다.
# 3. 가장 큰 안전 영역을 구함

import sys, copy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 바이러스 퍼뜨리기
def virus(x,y):
    global temp
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if temp[nx][ny] == 0 and not visited[nx][ny]:
            temp[nx][ny] = 2
            visited[nx][ny] = 1 # 방문표시
            virus(nx, ny)




# 벽 3개를 세우는 경우의 수
lst = []
answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            lst.append((i,j))

for c in set(combinations(lst, 3)):
    temp = copy.deepcopy(matrix)
    
    # 벽 세우기
    for a,b in c:
        temp[a][b] = 1
    visited = copy.deepcopy(temp)

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                virus(i, j)

    cnt = 0
    for i in range(N):
        cnt += temp[i].count(0)
    answer = max(answer, cnt)

print(answer)

