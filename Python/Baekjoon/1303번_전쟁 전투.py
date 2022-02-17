from collections import deque

# 위치 정하기
N, M = map(int,input().split())
field = [list(map(str,input())) for _ in range(M)] # 데이터 입력


dx = [1,0,-1,0]
dy = [0,1,0,-1]



