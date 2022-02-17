import sys
from collections import deque

N = int(input())
matrix = []
maxNum = 0


dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if matrix[i][j] > maxNum:
            maxNum = matrix[i][j]




def bfs(n):
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue

            if matrix[nx][ny] > n and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1



answer = 0
for i in range(maxNum):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for a in range(N):
        for b in range(N):
            if matrix[a][b] > i and visited[a][b]==0:
                queue.append((a,b))
                visited[a][b] = 1 # 방문처리
                bfs(i)
                cnt += 1
    answer = max(answer,cnt)

print(answer)


