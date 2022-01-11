N,M,V = map(int,input().split())

# 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)



# dfs
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
# bfs
# V = 1,
# queue = [1] #방문 노드 저장
# visited[1] = 1 => visited = [0][1][0][0][0]
# queue = []
# 1
# visited[2]==0 and graph[1][2]==1
# queue = [2]
# visited[3]==0 and graph[1][3]==1
# queue = [2],[3]
# visited[4]==0 and graph[1][4]==1
# queue = [2], [3], [4]
# while 반복
# queue = [3], [4]
# 2


# visited = [0,0,0,0,0]
#            1  2  3  4
#         1  0  1  1  1
#         2  1  0  0  1
#         3  1  0  0  1
#         4  1  1  1  0






