# 7-2) 11720번: 숫자의 합
N = int(input())
M = list(input())
result = 0
for i in M:
    result += int(i)
print(result)