# 3-4) 15552번: 빠른 A+B
import sys

T = int(input())  # input은 속도가 느려 여러개 입력시 sys를 import한 후 해당 함수를 사용.
# sys.stdin.readline() : 한 라인 입력 받을 떄
# sys.stdin() : 여러 줄 입력 받을 때
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)