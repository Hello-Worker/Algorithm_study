# 3-10) 별 찍기-2
N = int(input())
for i in range(N):
    i += 1
    print(" "*(N-i) +  "*" * i)