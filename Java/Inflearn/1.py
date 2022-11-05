import sys
sys.setrecursionlimit(10000)

def dfs(i, j, n, m, graph, visited):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if visited[i][j] == True:
        return 0

    if graph[i][j] == 0:
        return 0

    visited[i][j] = True

    for r in range(4):
        nx = i + dx[r]
        ny = j + dy[r]

        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue

        dfs(nx, ny, n, m, graph, visited)

    return 1


def solution():
    t = int(input())
    for _ in range(t):

        m, n, k = map(int, input().split())
        graph = [[0 for _ in range(m)] for _ in range(n)]

        for _ in range(k):
            i, j = map(int, input().split())
            graph[j][i] = 1

        visited = [[False for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1 and visited[i][j] == False:
                    ans += dfs(i, j, n, m, graph, visited)

        print(ans)

solution()