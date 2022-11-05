import sys

n = int(input())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
tmp = 0
answer = 0
for i in range(1,n+1):
    answer += sum[0:i]

print(answer)