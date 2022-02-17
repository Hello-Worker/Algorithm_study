# from collections import deque

# N = int(input())

# # 행렬 만들기
# graph = [list(map(int, input())) for _ in range(N)]


# def bfs(graph,x,y):

#     # 상하좌우
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     queue = deque()
#     queue.append((x,y))
#     graph[x][y] = 0  #탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함
#     cnt = 1
    
#     while queue:
#         x,y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= N or ny <0 or ny >= N:
#                 continue

#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx,ny))
#                 cnt += 1
#     return cnt

# count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

# count.sort()
# print(len(count))

# for i in range(len(count)):
#     print(count[i])


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
num = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
    if x<0 or x>=N or y<0 or y >=N:
        return False
    
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            DFS(nx,ny)
        return True
    return False
    

count = 0
result = 0

for i in range(N):
    for j in range(N): 
        if DFS(i,j) == True:
            num.append(count)
            result += 1
            count = 0
        
num.sort()
print(result)
for i in range(len(num)):
	print(num[i])
