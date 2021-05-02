# 선생님 T, 학생 S, 장애물 O, 빈칸 X
# N*N 행렬 - 데이터 받아서 리스트화
# O 3개 설치 가능 - 조합 이용해서 랜덤설치
# T는 상하좌우 확인 가능 - T의 위치확인, for문으로 확인, DFS
# 모두 숨길 수 있으면 YES 출력, 없을시 NO 출력

from itertools import combinations
from copy import deepcopy

N = int(input())
data = [list(map(str,input().split())) for _ in range(N)]

list_T = [] # 선생님 T의 위치
list_S = [] # 학생 S의 위치
list_X = [] # 빈칸 X의 위치

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# T, S, X 위치 찾기
for i in range(N):
    for j in range(N):
        if data[i][j] == 'T':
            list_T.append([i, j])
        if data[i][j] == 'S':
            list_S.append([i,j])
        if data[i][j] == 'X':
            list_X.append([i, j])

# DFS
def DFS(data, x, y, idx):
    if x < 0 or x >= N or y < 0 or y >= N or data[x][y] == 'O':
        return
    else:
        data[x][y] = 'T'
        DFS(data, x + dx[idx], y + dy[idx], idx)

# 상하좌우 확인: S를 만나지 않으면 True, S를 만나면 False를 리턴
def check():
    copy_data = deepcopy(data)
    for [x, y] in list_T:
        for i in range(4):
            DFS(copy_data, x, y, i)
    for [x, y] in list_S:
        if copy_data[x][y] != 'S':
            return False

    return True

# 빈칸에 조합으로 벽세우기.
for case in list(combinations(list_X, 3)):
    for [x, y] in case:
        data[x][y] = 'O'
    if check():
        print("YES")
        exit()
    for [x, y] in case:
        data[x][y] = 'X'

print("NO")


