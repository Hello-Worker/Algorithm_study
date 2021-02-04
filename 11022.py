# 3-8) A+B -8
import sys

T = int(input())
for i in range(1, T+1):
    a,b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i,a,b,a+b))
