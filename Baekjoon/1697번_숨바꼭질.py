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


# dist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 5 17

# queue = [5]
# x = 5
# dits[5] = 0
# nx = [4, 6, 10]

# nx = 4 and dist[4] = 0 #방문한적 없음
# dist[4] = 0+1 = 1

# nx = 6 and dist[6] = 0 #방문한적 없음
# dist[6] = 0+1 = 1

# nx = 10 and dist[10] = 0 #방문한 적 없음
# dist[10] = 0+1 = 1


# queue = [4,6,10]
# x = 4
# dist[4] = 1 #위에서 1
# nx = [3, 5, 8]

# nx = 3 and dist[3] = 0 
# dist[3] = 1+1 = 2

# nx = 5 and dist[5] = 0
# dist[5] = 1+1 = 2

# nx = 8 and dist[8] = 0
# dist[8] = 1+1 = 2


# queue = [6,10,3,5,8]
# x = 6
# dist[6] = 1
# nx = [5, 7, 12]

# nx = 5 and dist[5] != 0 # 다시 갔던 곳을 방문하는 것은 최단경로가 아님

# nx = 7 and dist[7] = 0
# dist[7] = 1+1 = 2

# nx = 12 and dist[12] = 0 
# dist[12] = 1+1 = 2


# queue = [10,3,5,8,7,12]
# x = 10
# dist[10] = 1
# nx = [9, 11, 20]

# nx = 9 and dist[9] = 0
# dist[9] = 1+1 = 2

# nx = 11 and dist[11] = 0
# dist[11] = 1+1 = 2

# nx = 20 and dist[20] = 0
# dist[20] = 1+1 = 2


# queue = [3,5,8,7,12,9,11,20]
# x = 3
# dist[3] = 2
# nx = [2, 4, 6]

# nx = 2 and dist[2] = 0
# dist[2] = 2+1 = 3

# nx = 4 and dist[4] != 0

# nx = 6 and dist[6] != 0


# queue = [5,8,7,12,9,11,20,2]
# x = 5
# dist[5] = 2
# nx = [4, 6, 10]

# queue = [8,7,12,9,11,20,2]
# x = 8
# dist[8] = 2
# nx = [7, 9, 16]

# dist[16] = 2+1 = 3

# queue = [7,12,9,11,20,2,16]
# x = 7
# dist[7] = 2
# nx = [6, 8, 14]
# dist[14] = 2+1 = 3

# queue = [12,9,11,20,2,16,14]
# x = 12
# dist[12] = 2
# nx = [11, 13, 24]

# dist[13] = 2+1 = 3
# dist[24] = 2+1 = 3

# queue = [9,11,20,2,16,14,13,24]
# x = 9
# dist[9] = 2
# nx = [8, 10, 18]
# dist[18] = 2+1 = 3

# queue = [11,20,2,16,14,13,24,18]
# x = 11
# dist[11] = 2
# nx = [10, 13, 22]

# dist[22] = 2+1 = 3

# queue = [20,2,16,14,13,24,18,22]
# x = 20
# dist[20] = 2
# nx = [19, 21, 40]

# dist[19] = 2+1 = 3
# dist[21] = 2+1 = 3
# dist[40] = 3+1 = 3

# queue = [2,16,14,13,24,18,22,19,21,40]
# x = 2
# dist[2] = 3
# nx = [1, 3, 4]
# dist[1] = 3+1 = 4

# queue = [16,14,13,24,18,22,19,21,40,1]
# x = 16
# dist[16] = 3
# nx = [15, 17, 32]

# dist[15] = 3+1 = 4
# dist[17] = 3+1 = 4 # 우리가 찾던 M은 4의 값을 가진다.
# if x == M:
#     print(dist[x])값은 4로 출력된다.

