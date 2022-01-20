from collections import deque

N, M  = map(int, input().split())

def BFS():
    queue = deque()
    queue.append(N)
    
    while queue:
        x = queue.popleft()
        if x == M:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx] = dist[x]+1
                queue.append(nx)
        
MAX = 100000
dist = [0] * (MAX+1)
N, M = map(int, input().split())
BFS()
