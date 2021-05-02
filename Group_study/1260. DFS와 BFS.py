N,M,V = map(int,input().split())

# 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visited = [0]*(N+1)

#dfs 함수 만들기
def dfs(V):
    visited[V] = 1 #방문처리
    print(V, end='')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited[V] = 0
    while queue:
        V = queue.pop(0)









# V = 1,
# visited[1] = 1 , visited = [0][1][0][0][0] => 1방문
# 1 프린트
# i == 2 일 때,
# graph[1][2] == 1 이고, visited[2] == 0 => 1에 연결되고, 방문한 적 없는 2를 선택
# 2에가서 dfs 재귀
#
# V = 2,
# visited[2] = 2, visited = [0][1][1][0][0] => 2방문
# graph[2][4] == 이고, visited[4] == 0 => 2에 연결되고, 방문한 적 없는 4를 선택
# 4에가서 dfs 재귀
#
# visited = [0,0,0,0,0]
#            1  2  3  4
#         1  0  1  1  1
#         2  1  0  0  1
#         3  1  0  0  1
#         4  1  1  1  0






