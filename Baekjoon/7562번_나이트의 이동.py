import sys
from collections import deque


t = int(input()) 

for _ in range(t):
    n = int(input())
    now = list(map(int, sys.stdin.readline().split()))
    dest = list(map(int, sys.stdin.readline().split()))   

    matrix = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    queue = deque()
    
    # 시계방향
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]


    def bfs():
        queue.append(now)
        visited[now[0]][now[1]]

        while queue:
            x, y = queue.popleft()

            if x == dest[0] and y == dest[1] :
                return 0

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx <0 or nx>=n or ny<0 or ny>=n:
                    continue

                if nx == dest[0] and ny == dest[1]:
                    visited[nx][ny] = True
                    return matrix[x][y]+1

                if visited[nx][ny] == False:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    matrix[nx][ny] = matrix[x][y] + 1    
    
    answer = bfs()
    print(answer)


    
