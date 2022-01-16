from collections import deque
N = int(input()) # 컴퓨터 수 
M = int(input()) # 컴퓨터 연결 수 

graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0]*(N+1)

def BFS(V):
    queue = deque()
    queue.append(V)
    visited[V] = 1
    cnt = 0

    while queue:
        V = queue.popleft()
        for i in range(1, N+1):
            if graph[V][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt
print(BFS(1))