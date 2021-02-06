# 3-11) 10871번: x보다 작은 수 (복습)
import sys

N, X = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))  # list로 각 숫자에 인덱스 부여
for i in A:
    if i < X:
        print(i, end=" ")  # end=" " 공백으로 띄울 것