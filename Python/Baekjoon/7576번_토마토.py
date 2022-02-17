from collections import deque
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
res = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i,j))

def BFS():
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] +1
                queue.append((nx,ny)) 

BFS()

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    
    res = max(res, max(i))
print(res-1)

