from collections import deque
N, M = map(int, input().split())

graph = [list(map(int,input())) for _ in range(N)]

# bfs
def bfs(x, y): 
    dx = [-1, 1, 0, 0] # 상하좌우 
    dy = [0, 0, -1, 1]

    queue = [[x,y]]
    
    while queue:
        x,y = queue.pop(0)
        
        # 현재 위치에서 동서남북 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 규격을 넘을 수 없는 조건
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
        
            # 벽이면 진행 불가
            if graph[nx][ny] == 0:
                continue

            # 벽이 없을 때 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx,ny))

    return graph[N-1][M-1]

print(bfs(0,0))

# (1,1)
# i = 0 : nx = 0, ny = 1 규격 넘어서 continue
# i = 1 : nx = 2, ny = 1  진행