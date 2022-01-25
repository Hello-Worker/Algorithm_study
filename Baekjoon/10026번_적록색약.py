import sys
from collections import deque

#n = int(input())
#matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

R = 'R'
B = 'B'
G = 'G'


n = 5
matrix = [[R,R,R,B,B],[G,G,B,B,B],[B,B,B,R,R],[B,B,R,R,R],[R,R,R,R,R]]
# 방문행렬
visited1 = [[0]*n for _ in range(n)]
visited2 = [item[:] for item in visited1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()

def noseakyak():



def seakyak():


cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:

            noseakyak()
            cnt1 += 1
        if visited2[i][j] == 0:
            seakyak()
            cnt2 += 1