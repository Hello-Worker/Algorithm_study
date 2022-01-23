from collections import deque
import sys

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
queue = deque()
answer = []

def bfs(x, y):   
    queue.append((x,y))
    matrix[x][y] = 0

    while queue:
        
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if matrix[nx][ny] == 1:
                queue.append((nx,ny))
                matrix[nx][ny] = 0
while True:
    n= list(map(int, input().split()))
    M = n[0]
    N = n[1]
    cnt = 0

    if M==0 and N==0:
        break
    else:
        matrix = [list(map(int, input().split())) for _ in range(n[1])]
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    bfs(i,j)
                    cnt+=1
        answer.append(cnt)
 
for i in answer:
    print(i)