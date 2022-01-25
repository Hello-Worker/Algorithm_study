import sys
from collections import deque

n = int(input())
matrix = [list(map(str, sys.stdin.readline())) for _ in range(n)]


# 방문행렬
visited1 = [[0]*n for _ in range(n)]
visited2 = [item[:] for item in visited1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()

def noseakyak():
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if matrix[x][y] == matrix[nx][ny] and visited1[nx][ny] == 0:
                queue.append((nx,ny))
                visited1[nx][ny] = 1
def seakyak():
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if visited2[nx][ny] == 0:
                if matrix[x][y] == matrix[nx][ny] or matrix[x][y] == 'R' and matrix[nx][ny] == 'G' or matrix[x][y] == 'G' and matrix[nx][ny] == 'R':
                    queue.append((nx,ny))
                    visited2[nx][ny] = 1

cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            queue.append((i,j))
            visited1[i][j] = 1
            noseakyak()
            cnt1 += 1
        if visited2[i][j] == 0:
            queue.append((i,j))
            visited2[i][j] = 1
            seakyak()
            cnt2 += 1

print(cnt1, cnt2)

# matrix1 = [list(map(str,input())) for _ in range(2)]
# matrix2 = [list(map(str,input().split())) for _ in range(2)]

# print(matrix1)
# print(matrix2)